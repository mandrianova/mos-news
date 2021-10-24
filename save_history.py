import json
import pandas as pd
import os

with open(os.path.join('data', 'news.json'), "r", encoding="utf_8_sig") as news_json:
    data = json.loads(news_json.read())

news_types = set()

for i in data:
    news_types.add(str(i.get('id'))[-3:])

print(news_types)

"""
073 - новости, 050 - новости мэра. news_types хотела определить 
какие вообще нам выдали типы, так как есть еще другие.
"""

df = pd.read_excel(os.path.join('data', 'dataset_news_1.xlsx'))


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
df_user_news = df[['user_id', 'date_time', 'news_id']]
df_news = pd.DataFrame.from_dict(data)
df_news = df_news[['id', 'title']].rename(columns={'id': 'news_id', 'title': 'title'})
df_merge = df_user_news.merge(df_news, how='inner', on='news_id')

result = {}

for index, row in df_merge.iterrows():
    user_id = row['user_id']
    news_id = row['news_id']
    title = row['title']
    date = row['date_time'].strftime(format="%Y-%m-%d %H:%M")
    if user_id not in result:
        result[user_id] = [{
            'id': news_id,
            'title': title,
            'date': date
        }]
    elif user_id in result:
        result[user_id].append({
            'id': news_id,
            'title': title,
            'date': date
        })

with open(os.path.join('data', 'history.json'), 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False,  indent=4)


