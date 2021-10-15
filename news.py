import json
import pandas as pd

with open('news.json', "r", encoding="utf_8_sig") as news_json:
    data = json.loads(news_json.read())

news_types = set()

for i in data:
    news_types.add(str(i.get('id'))[-3:])

print(news_types)

"""
073 - новости, 050 - новости мэра. news_types хотела определить 
какие вообще нам выдали типы, так как есть еще другие.
"""

df = pd.read_excel('dataset_news_1.xlsx')


def get_news_id_from_url(url: str) -> int:
    """
    Вычленить id из url
    """
    parts = url.split('/')
    try:
        if parts[-2] == '9468':
            print(url)
        return int(parts[-2])
    except Exception as err:
        print(url)
        for part in parts:
            if '073' in part:  # Опытным путем выявлено, что битые урлы
                # только для типа 073, поэтому просто решила вытащить такие
                return int(part)
        print("it is not news url ", url)
        return 0


def get_news_type(news_id: int) -> str:
    """
    Ради понимания структуры данных, получить тип новости из id,
    также найти ошибочные id (нашла таких 3 штуки)
    """
    if str(news_id)[-3:] == '073':
        return "news"
    if str(news_id)[-3:] == '050':
        return "major"
    else:
        print(news_id)
        return "error"


df['news_id'] = df['url_clean'].apply(get_news_id_from_url)
df['news_type'] = df['news_id'].apply(get_news_type)

df['news_type'].value_counts()

news_ids_from_ds = set(df['news_id'].unique())
news_ids_from_json = set([i.get('id') for i in data])

# Тут можно посравнивать два сета и увидеть разницу в списке id

df_json = pd.read_json('news.json', encoding="utf_8_sig")  # Закинем json в df
df_json["news_type"] = df_json['id'].apply(get_news_type)
df_json["news_type"].value_counts()

with open('districts.json', "r", encoding="utf_8_sig") as file:
    data_districts = json.loads(file.read())

districts = list()
for a in data_districts["items"]:
    for d in a['areas']:
        d['area_title'] = a['title']
        d['area_local_id'] = a['local_id']
        districts.append(d)
    if not a['areas']:
        districts.append({
            "id": a['id'],
            "title": a['title'],
            "local_id": a['local_id'],
            "district_id": None,
            "site": None,
            "population": None,
            "square": None,
            "manager_id": None,
            "title_en": a['title_en'],
            'area_title': a['title'],
            'area_local_id': a['local_id']
        })

districts_df = pd.DataFrame(districts)

