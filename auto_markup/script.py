import os
import pandas as pd
import json
import urllib.request, json
from itertools import islice
from typing import Iterator
import re
from nltk.corpus import stopwords
from collections import Counter
import math
import pymorphy2

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

# очитска full_text
patterns_to_replace = {
    '&nbsp;': ' ',  # замена пробела(&nbsp;) на пробел
    '<.+?>|\\n|&[a-z]+;': '',  # замена всех тэгов, /n и выражений типа &ldquo; на пустую строку
    '\s+': ' ',  # замена всех повторяющихся пробелов на один
    '(.\.)(\S)': '\g<1> \g<2>',
    # добавление пробела после конца предложения, если дальше нет пробела и начинается буква
    '\s+$': '',  # удаление пробелов с конца строки
}


def get_text_on_pattern_replacement_func(patterns_to_replace: dict, html_text: str) -> str:
    for pattern, repl in patterns_to_replace.items():
        html_text = re.sub(pattern, repl, html_text)
        return html_text


def get_lst_of_normalized_tokens_without_stopwords(text, is_normalize=IS_NORMALIZE):
    pattern = re.compile(r"([-\s.,;!?])+")
    tokens = pattern.split(text)
    tokens = [x for x in tokens if x not in STOP_WORDS and x not in '- \t\n.,;!?' and not x[0].isupper() and len(x) > 2 and x.isalpha()]
    if is_normalize:
        first_filter = [morph.normal_forms(x)[0] for x in tokens]
        return [x for x in first_filter if x not in STOP_WORDS]

    return tokens


# tags lst of dicts(objects)
lst_of_tags_objects = tags_json['tags']
# set of tags
set_of_tags = set([tag['title'] for tag in lst_of_tags_objects])

# spheres lst of dicts(objects)
all_spheres_lst_of_objects = spheres_json1['items'] + spheres_json2['items']
# set_of_spehres
set_of_spheres = set([sphere['title'] for sphere in all_spheres_lst_of_objects])


def get_corpus():
    '''Проходит циклом по всем новостям, забирает html новость,
    проходит регуляркой, достает токены, фильтрует и запихивает в список, формирует список списков'''

    corpus = []
    for one_news in news:
        if 'full_text' in one_news:
            full_txt = get_text_on_pattern_replacement_func(patterns_to_replace, one_news['full_text'])
            lst_of_tokens_without_stopwords = get_lst_of_normalized_tokens_without_stopwords(text=full_txt,
                                                                                             is_normalize=True)
            corpus.append(list(set(lst_of_tokens_without_stopwords)))
    return corpus


def compute_tf(text):
    txt = get_text_on_pattern_replacement_func(patterns_to_replace, text)
    tokens_without_stopwords = get_lst_of_normalized_tokens_without_stopwords(txt)
    count_of_words = Counter(tokens_without_stopwords)
    for key in count_of_words:
        count_of_words[key] = count_of_words[key] / float(len(text))
    return count_of_words


def compute_idf(word, corpus):
    # на вход берется слово, для которого считаем IDF
    # и корпус документов в виде списка списков слов
    # количество документов, где встречается искомый термин
    # считается как генератор списков
    # как хранить corpus?
    return math.log10(len(corpus) / sum([1 for lst_of_tokens in corpus if word in lst_of_tokens]))


def match_weight_with_exist_tag(word, tags, weight_with_exist_tag=WEIGHT_EXIST_TAG):
    # на вход берется слово, проверяем его в тегах
    return WEIGHT_EXIST_TAG if word in tags else 1


def get_result_tags(number_of_one_news, corpus):
    tf_idf_dictionary = {}
    computed_tf = compute_tf(news[number_of_one_news]['full_text'])
    for word in computed_tf:
        tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus) * match_weight_with_exist_tag(word, set_of_tags)
        # documents_list.append(tf_idf_dictionary)
    sorted_tuples = sorted(tf_idf_dictionary.items(), key=lambda item: item[1], reverse=True)

    print('RESULT: \n', [i for i, j in sorted_tuples[:10]])
    print('TAGS: \n', [tag['title'] for tag in news[number_of_one_news]['tags']], '\n')


def get_examples_for_n_news(n):
    corpus = get_corpus()
    for i in range(n):
        get_result_tags(i, corpus)