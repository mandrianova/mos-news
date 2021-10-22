import os
import pymorphy2
import urllib.request
import json
import pickle

from auto_markup.support_for_model.support_decorators import measure_exectime, try_except_none_wrapper
from auto_markup.support_for_model.text_manipulation import get_text_on_pattern_replacement_func, \
    get_lst_of_normalized_tokens_without_stopwords

morph = pymorphy2.MorphAnalyzer()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
path_to_data_folder = os.path.join(BASE_DIR, 'data')

source_xlsx = os.path.join(path_to_data_folder, 'dataset_news_1.xlsx')
source_json = os.path.join(path_to_data_folder, 'save_history.json')
source_districts_json = os.path.join(path_to_data_folder, 'districts.json')
source_corpus = os.path.join(path_to_data_folder, 'data_auto_markup', 'corpus.pickle')
source_set_of_tags = os.path.join(path_to_data_folder, 'data_auto_markup', 'tags.pickle')
source_normalized_set_of_tags = os.path.join(path_to_data_folder, 'data_auto_markup', 'normalized_tags.pickle')
source_set_of_spheres = os.path.join(path_to_data_folder, 'data_auto_markup', 'set_of_spheres.pickle')
source_normalized_set_of_spheres = os.path.join(path_to_data_folder, 'data_auto_markup',
                                                'normalized_set_of_spheres.pickle')
source_dict_normalized_tag_spheres = os.path.join(path_to_data_folder, 'data_auto_markup',
                                                  'dict_normalized_tag_spheres.pickle')


def get_news(path=source_json):
    with open(path, "r", encoding="utf_8_sig") as news_json:
        news = json.loads(news_json.read())
        return news


@try_except_none_wrapper
@measure_exectime
def save_set_of_tags(html="https://www.mos.ru/aisearch/suggest/ais/api/tags/", path=source_set_of_tags):
    with urllib.request.urlopen(html) as url:
        tags_json = json.loads(url.read().decode())
        lst_of_tags_objects = tags_json['tags']
        set_of_tags = set([tag['title'] for tag in lst_of_tags_objects])
    with open(path, 'wb') as f:
        pickle.dump(set_of_tags, f)


@measure_exectime
def get_set_of_tags(path=source_set_of_tags):
    if os.path.isfile(path):
        print('Set of tags found.')
        with open(path, 'rb') as f:
            set_of_tags = pickle.load(f)
            return set_of_tags
    print('Set of tags not found')
    return None


@try_except_none_wrapper
@measure_exectime
def save_normalized_set_of_tags(*, set_of_tags, path=source_normalized_set_of_tags):
    normalized_set_of_tags = [morph.normal_forms(x)[0] for x in set_of_tags if len(x.split()) == 1]
    with open(path, 'wb') as f:
        pickle.dump(normalized_set_of_tags, f)


def get_normalized_set_of_tags(path=source_normalized_set_of_tags):
    if os.path.isfile(source_normalized_set_of_tags):
        print('Set of normalized tags found.')
        with open(path, 'rb') as f:
            normalized_set_of_tags = pickle.load(f)
            return normalized_set_of_tags
    print('Set of normalized tags not found')
    return None


@try_except_none_wrapper
@measure_exectime
def save_set_of_spheres(path=source_set_of_spheres):
    with urllib.request.urlopen(
            "https://www.mos.ru/api/newsfeed/v4/frontend/json/ru/spheres?fields=id%2Ctitle&per-page=50&page=1") as url:
        spheres_json1 = json.loads(url.read().decode())
    with urllib.request.urlopen(
            "https://www.mos.ru/api/newsfeed/v4/frontend/json/ru/spheres?fields=id%2Ctitle&per-page=50&page=2") as url:
        spheres_json2 = json.loads(url.read().decode())
    all_spheres_lst_of_objects = spheres_json1['items'] + spheres_json2['items']
    set_of_spheres = set([sphere['title'] for sphere in all_spheres_lst_of_objects])
    with open(path, 'wb') as f:
        pickle.dump(set_of_spheres, f)


def get_set_of_spheres(path=source_set_of_spheres):
    if os.path.isfile(path):
        print('Set of spheres found.')
        with open(path, 'rb') as f:
            normalized_set_of_tags = pickle.load(f)
            return normalized_set_of_tags
    print('Set of normalized tags not found')
    return None


@try_except_none_wrapper
@measure_exectime
def save_normalized_set_of_spheres(*, set_of_spheres, path=source_normalized_set_of_spheres):
    normalized_set_of_spheres = [morph.normal_forms(x)[0] for x in set_of_spheres if len(x.split()) == 1]
    with open(path, 'wb') as f:
        pickle.dump(normalized_set_of_spheres, f)


def get_normalized_set_of_spheres(path=source_normalized_set_of_spheres):
    if os.path.isfile(path):
        print('Set of normalized tags found.')
        with open(path, 'rb') as f:
            normalized_set_of_spheres = pickle.load(f)
            return normalized_set_of_spheres
    print('Set of normalized tags not found')
    return None


# dict tag - set of spheres
@try_except_none_wrapper
@measure_exectime
def save_dict_normalized_tag_spheres(*, news, path=source_dict_normalized_tag_spheres):
    dict_tag_spheres = {}
    for one_news in news:
        if 'tags' in one_news and 'spheres' in one_news:
            spheres_list = []
            for sphere_object in one_news['spheres']:
                spheres_list.append(sphere_object['title'])

            normalized_tag_list = []
            for tag_object in one_news['tags']:
                if len(tag_object['title'].split()) < 2:
                    normalized_tag_list.append(morph.normal_forms(tag_object['title'])[0])
                else:
                    normalized_tag_list.append(tag_object['title'])
            for normalized_tag in normalized_tag_list:
                if normalized_tag in dict_tag_spheres:
                    dict_tag_spheres[normalized_tag] = dict_tag_spheres[normalized_tag].intersection(spheres_list)
                else:
                    dict_tag_spheres[normalized_tag] = set(spheres_list)
    with open(path, 'wb') as f:
        pickle.dump(dict_tag_spheres, f)


def get_dict_normalized_tag_spheres(path=source_dict_normalized_tag_spheres):
    if os.path.isfile(path):
        print('Dict normalized tag spheres of normalized tags found.')
        with open(path, 'rb') as f:
            dict_normalized_tag_spheres = pickle.load(f)
            return dict_normalized_tag_spheres
    print('Dict normalized tag spheres of normalized tags not found.')
    return None


@try_except_none_wrapper
@measure_exectime
def save_corpus(path=source_corpus):
    corpus = []
    news = get_news()
    n = 0
    for one_news in news:
        if 'full_text' in one_news:
            full_txt = get_text_on_pattern_replacement_func(one_news['full_text'])
        elif 'text' in one_news:
            full_txt = get_text_on_pattern_replacement_func(one_news['text'])
        else:
            full_txt = None
            print('full_text is None')
        if 'preview_text' in one_news:
            preview_text = get_text_on_pattern_replacement_func(one_news['preview_text'])
        elif 'preview' in one_news:
            preview_text = get_text_on_pattern_replacement_func(one_news['preview'])
        else:
            preview_text = None
            print('preview_text is None')
        if 'title' in one_news:
            title = get_text_on_pattern_replacement_func(one_news['title'])
        else:
            title = None
            print('title is None')
        if all(map(lambda a: isinstance(a, type(None)), [title, preview_text, full_txt])):
            n += 1
            continue
        else:
            list_of_not_none_fields = list(
                filter(lambda a: not isinstance(a, type(None)), [title, preview_text, full_txt])
            )
            sum_txt = ' '.join(list_of_not_none_fields)
        lst_of_tokens_without_stopwords = get_lst_of_normalized_tokens_without_stopwords(
            text=sum_txt,
            is_normalize=True
        )
        corpus.append(list(set(lst_of_tokens_without_stopwords)))
    print(f'All fields(full_text, title, preview_text) is None together {n} times')
    with open(path, 'wb') as f:
        pickle.dump(corpus, f)


def get_corpus():
    """Проходит циклом по всем новостям, забирает html новость,
    проходит регуляркой, достает токены, фильтрует и запихивает в список, формирует список списков"""
    if os.path.isfile(source_corpus):
        print('Corpus found.')
        with open(source_corpus, 'rb') as f:
            corpus = pickle.load(f)
            return corpus
    print('Corpus not found')
    return None


def save_all_files():
    save_set_of_tags()
    set_of_tags = get_set_of_tags()
    save_normalized_set_of_tags(set_of_tags=set_of_tags)
    save_set_of_spheres()
    set_of_spheres = get_set_of_spheres()
    save_normalized_set_of_spheres(set_of_spheres=set_of_spheres)
    save_corpus()
    news = get_news()
    save_dict_normalized_tag_spheres(news=news)
    return True
