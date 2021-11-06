import requests
from requests import HTTPError

from auto_markup.support_for_model.text_manipulation import get_text_on_pattern_replacement_func


def get_one_news_from_mos_api(news_id: int):
    if str(news_id).endswith('050'):
        type_of_news = '050'
        link = f'https://www.mos.ru/api/newsfeed/v4/frontend/json/ru/press' \
               f'/news/{news_id}?expand=spheres&fields=id,title,text,preview,tags,spheres'
    elif str(news_id).endswith('073'):
        type_of_news = '073'
        link = f'https://www.mos.ru/api/newsfeed/v4/frontend/json/ru' \
               f'/articles/{news_id}?expand=spheres&fields=id,title,full_text,preview_text,tags,spheres'
    else:
        raise ValueError

    request = requests.get(link)
    if request.status_code != 200:
        raise HTTPError

    request_dict = request.json()
    data = {}
    try:
        data['id'] = request_dict['id']
        data['tags'] = [tag['title'] for tag in request_dict['tags']]
        data['spheres'] = [sphere['title'] for sphere in request_dict['spheres']]
        if type_of_news == '050':
            data['title'] = get_text_on_pattern_replacement_func(request_dict['title'])
            data['preview_text'] = get_text_on_pattern_replacement_func(request_dict['preview'])
            data['full_text'] = get_text_on_pattern_replacement_func(request_dict['text'])
        elif type_of_news == '073':
            data['title'] = get_text_on_pattern_replacement_func(request_dict['title'])
            data['preview_text'] = get_text_on_pattern_replacement_func(request_dict['preview_text'])
            data['full_text'] = get_text_on_pattern_replacement_func(request_dict['full_text'])
    except Exception as er:
        print(er)

    return data
