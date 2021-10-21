from auto_markup.support_for_model.support_decorators import measure_exectime
from auto_markup.support_for_model.text_manipulation import get_text_on_pattern_replacement_func, \
    get_lst_of_normalized_tokens_without_stopwords, STOP_WORDS
from auto_markup.support_for_model.work_with_files import get_corpus, get_normalized_set_of_tags, get_news, \
    get_dict_normalized_tag_spheres, save_all_files
from collections import Counter
import math
from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    Doc
)


WEIGHT_EXIST_TAG = 2


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
    # markup = ner_tagger(text)
    # markup.print()
    for span in doc.spans:
        span.normalize(morph_vocab)
    named_objects = set([_.normal for _ in doc.spans])
    named_objects_without_stop_words = set(
        [named_object for named_object in named_objects if named_object.lower() not in STOP_WORDS])
    return named_objects_without_stop_words


def compute_tf(text):
    txt = get_text_on_pattern_replacement_func(text)
    tokens_without_stopwords = get_lst_of_normalized_tokens_without_stopwords(txt)
    count_of_words = Counter(tokens_without_stopwords)
    for key in count_of_words:
        count_of_words[key] = count_of_words[key] / float(len(tokens_without_stopwords))
    return count_of_words


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


@measure_exectime
def get_result_tag_and_spheres_for_title_preview_fulltext(*, title, preview, full_txt):
    corpus = get_corpus()
    if corpus is None:
        return None
    full_txt = get_text_on_pattern_replacement_func(full_txt)
    text = ' '.join([title, preview, full_txt])
    tf_idf_dictionary = {}
    computed_tf = compute_tf(text)
    normalized_set_of_tags = get_normalized_set_of_tags()
    for word in computed_tf:
        tf_idf_dictionary[word] = computed_tf[word]\
                                  * compute_idf(word, corpus)\
                                  * match_weight_with_exist_tag(word, normalized_set_of_tags)
    sorted_tuples = sorted(tf_idf_dictionary.items(), key=lambda item: item[1], reverse=True)
    ordinary_tags = set([i for i, j in sorted_tuples[:10]])
    named_objects_without_stopwords = get_named_objects_without_stopwords(text)
    all_tags = ordinary_tags.union(named_objects_without_stopwords)
    dict_normalized_tag_spheres = get_dict_normalized_tag_spheres()
    set_of_spheres = set()
    for tag in all_tags:
        if tag in dict_normalized_tag_spheres:
            set_of_spheres.update(dict_normalized_tag_spheres[tag])
    return list(all_tags), list(set_of_spheres)


def check_function(number_of_news):
    news = get_news()
    title = news[number_of_news]['title']
    preview_text = news[number_of_news]['preview_text']
    full_text = news[number_of_news]['full_text']
    tags, set_of_spheres = get_result_tag_and_spheres_for_title_preview_fulltext(
        title=title,
        preview_text=preview_text,
        full_txt=full_text
    )
    print('RESULT TAGS: \n', tags)
    print('RESULT SPHERES: \n', set_of_spheres)
    print('REAL TAGS: \n', [tag_object['title'] for tag_object in news[number_of_news]['tags']])
    print('REAL SPHERES: \n', [sphere_object['title'] for sphere_object in news[number_of_news]['spheres']])


def update_model_func():
    try:
        save_all_files()
        return True
    except Exception as ex:
        print(ex)
        return None