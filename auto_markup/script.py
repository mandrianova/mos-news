import os
import pandas as pd
import json
import pickle
import urllib.request, json
import re
from nltk.corpus import stopwords
from collections import Counter
import math
import pymorphy2
from functools import lru_cache
from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    Doc
)

IS_NORMALIZE = True
WEIGHT_EXIST_TAG = 2
STOP_WORDS = stopwords.words("russian")
STOP_WORDS_MONTHS = ['сентябрь', 'октябрь', 'ноябрь', 'декабрь', 'январь', 'февраль', 'март', 'апрель', 'март', 'май',
                     'июнь', 'июль', 'август']
STOP_WORDS += STOP_WORDS_MONTHS

morph = pymorphy2.MorphAnalyzer()

path_to_folder = 'C:\\Users\\mrrax\\projects\\mos-news'
source_xlsx = os.path.join(path_to_folder, 'dataset_news_1.xlsx')
source_json = os.path.join(path_to_folder, 'news.json')
source_districts_json = os.path.join(path_to_folder, 'districts.json')

with open(source_json, "r", encoding="utf_8_sig") as news_json:
    news = json.loads(news_json.read())
with open(source_districts_json, "r", encoding="utf_8_sig") as news_json:
    source_districts_json = json.loads(news_json.read())
with urllib.request.urlopen("https://www.mos.ru/aisearch/suggest/ais/api/tags/") as url:
    tags_json = json.loads(url.read().decode())
with urllib.request.urlopen(
        "https://www.mos.ru/api/newsfeed/v4/frontend/json/ru/spheres?fields=id%2Ctitle&per-page=50&page=1") as url:
    spheres_json1 = json.loads(url.read().decode())
with urllib.request.urlopen(
        "https://www.mos.ru/api/newsfeed/v4/frontend/json/ru/spheres?fields=id%2Ctitle&per-page=50&page=2") as url:
    spheres_json2 = json.loads(url.read().decode())


def get_text_on_pattern_replacement_func(html_text: str) -> str:
    patterns_to_replace = {
        '&nbsp;|&ndash;': ' ',  # замена пробела(&nbsp;) на пробел
        '<.+?>|\\n|&[a-z]+;': '',  # замена всех тэгов, /n и выражений типа &ldquo; на пустую строку
        '\s+': ' ',  # замена всех повторяющихся пробелов на один
        '(.\.)(\S)': '\g<1> \g<2>',
        # добавление пробела после конца предложения, если дальше нет пробела и начинается буква
        '\s+$': '',  # удаление пробелов с конца строки
        '(.\.)\s(ru)': '\g<1>\g<2>',  # если после любого символа идет точка и пробел и за ним ru, то уберет пробел
        '([а-я])([А-Я])': '\g<1>. \g<2>',  # если после а-я (low) большие А-Я (high), между ними вставит точку и пробел
    }

    for pattern, repl in patterns_to_replace.items():
        html_text = re.sub(pattern, repl, html_text)
    return html_text


@lru_cache(maxsize=16384)
def get_lst_of_normalized_tokens_without_stopwords(text, is_normalize=IS_NORMALIZE):
    pattern = re.compile(r"([-\s.,;!?])+")
    tokens = pattern.split(text)
    tokens = [x for x in tokens if
              x not in STOP_WORDS and x not in '- \t\n.,;!?' and not x[0].isupper() and len(x) > 2 and x.isalpha()]
    if is_normalize:
        first_filter = [morph.normal_forms(x)[0] for x in tokens]
        return [x for x in first_filter if x not in STOP_WORDS]

    return tokens


def get_named_objects_without_stopwords(text):
    segmenter = Segmenter()
    morph_vocab = MorphVocab()
    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)
    syntax_parser = NewsSyntaxParser(emb)
    ner_tagger = NewsNERTagger(emb)

    text = get_text_on_pattern_replacement_func(text)
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    doc.tag_ner(ner_tagger)
    markup = ner_tagger(text)
    markup.print()
    for span in doc.spans:
        span.normalize(morph_vocab)
    named_objects = set([_.normal for _ in doc.spans])
    named_objects_without_stop_words = set(
        [named_object for named_object in named_objects if named_object.lower() not in STOP_WORDS])
    return named_objects_without_stop_words


# tags lst of dicts(objects)
lst_of_tags_objects = tags_json['tags']
# set of tags
set_of_tags = set([tag['title'] for tag in lst_of_tags_objects])

# spheres lst of dicts(objects)
all_spheres_lst_of_objects = spheres_json1['items'] + spheres_json2['items']
# set_of_spehres
set_of_spheres = set([sphere['title'] for sphere in all_spheres_lst_of_objects])


# @lru_cache(maxsize=10000)
def get_corpus():
    '''Проходит циклом по всем новостям, забирает html новость,
    проходит регуляркой, достает токены, фильтрует и запихивает в список, формирует список списков'''
    if os.path.isfile('corpus.pickle'):
        with open('corpus.pickle', 'rb') as f:
            corpus = pickle.load(f)
            return corpus
    corpus = []
    for one_news in news:
        if 'full_text' in one_news:
            full_txt = get_text_on_pattern_replacement_func(one_news['full_text'])
            lst_of_tokens_without_stopwords = get_lst_of_normalized_tokens_without_stopwords(text=full_txt,
                                                                                             is_normalize=True)
            corpus.append(list(set(lst_of_tokens_without_stopwords)))

    with open('corpus.pickle', 'wb') as f:
        pickle.dump(corpus, f)
    return corpus


def compute_tf(text):
    txt = get_text_on_pattern_replacement_func(text)
    tokens_without_stopwords = get_lst_of_normalized_tokens_without_stopwords(txt)
    count_of_words = Counter(tokens_without_stopwords)
    for key in count_of_words:
        count_of_words[key] = count_of_words[key] / float(len(text))
    return count_of_words


# @lru_cache(maxsize=10000)
def compute_idf(word, corpus):
    # на вход берется слово, для которого считаем IDF
    # и корпус документов в виде списка списков слов
    # количество документов, где встречается искомый термин
    # считается как генератор списков
    # как хранить corpus?
    sum_unique = sum([1 for lst_of_tokens in corpus if word in lst_of_tokens])
    if sum_unique == 0:
        return 2
    return math.log10(len(corpus) / sum_unique)


def match_weight_with_exist_tag(word, tags, weight_with_exist_tag=WEIGHT_EXIST_TAG):
    # на вход берется слово, проверяем его в тегах
    return weight_with_exist_tag if word in tags else 1


def get_result_tags(number_of_one_news, corpus):
    tf_idf_dictionary = {}
    computed_tf = compute_tf(news[number_of_one_news]['full_text'])
    for word in computed_tf:
        tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus) * match_weight_with_exist_tag(word, set_of_tags)
        # documents_list.append(tf_idf_dictionary)
    sorted_tuples = sorted(tf_idf_dictionary.items(), key=lambda item: item[1], reverse=True)
    ordinary_tags = set([i for i, j in sorted_tuples[:10]])
    named_objects_without_stopwords = get_named_objects_without_stopwords(news[number_of_one_news]['full_text'])
    all_tags = ordinary_tags.union(named_objects_without_stopwords)
    print('RESULT to ordinary: \n', ordinary_tags)
    print('RESULT to named objects: \n', named_objects_without_stopwords)
    print('TAGS: \n', [tag['title'] for tag in news[number_of_one_news]['tags']], '\n')


# def get_examples_for_n_news(n):
#     corpus = get_corpus()
#     for i in range(n):
#         get_result_tags(i, corpus)
#
#
# get_examples_for_n_news(10)
# get_lst_of_normalized_tokens_without_stopwords.cache_info()

with urllib.request.urlopen("https://www.mos.ru/api/newsfeed/v4/frontend/json/ru/articles/97616073?expand=spheres&fields=id,title,label,tags,date,date_timestamp,kind,place,free,department_id,full_text,preview_text") as url:
    new_news = json.loads(url.read().decode())


def get_result_tags_for_new_news(text, corpus):
    tf_idf_dictionary = {}
    computed_tf = compute_tf(text)
    for word in computed_tf:
        tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus) * match_weight_with_exist_tag(word, set_of_tags)
        # documents_list.append(tf_idf_dictionary)
    sorted_tuples = sorted(tf_idf_dictionary.items(), key=lambda item: item[1], reverse=True)
    ordinary_tags = set([i for i, j in sorted_tuples[:10]])
    named_objects_without_stopwords = get_named_objects_without_stopwords(text)
    all_tags = ordinary_tags.union(named_objects_without_stopwords)
    print('RESULT to ordinary: \n', ordinary_tags)
    print('RESULT to named objects: \n', named_objects_without_stopwords)