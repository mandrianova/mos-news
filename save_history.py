import json
import pandas as pd

with open('data/news.json', "r", encoding="utf_8_sig") as news_json:
    data = json.loads(news_json.read())

news_types = set()

for i in data:
    news_types.add(str(i.get('id'))[-3:])

print(news_types)

"""
073 - новости, 050 - новости мэра. news_types хотела определить 
какие вообще нам выдали типы, так как есть еще другие.
"""

df = pd.read_excel('data/dataset_news_1.xlsx')


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
    date = str(row['date_time'])
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

with open('data/history.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False,  indent=4)


# lst_of_user_id = sorted(list(df_merge['user_id'].unique()))
#
# result = []
# for user_id in lst_of_user_id:
#     obj = {
#         'user_id': int(user_id),
#         'history': []
#     }
#     df_for_user = df_merge[df_merge.user_id == user_id]
#     for index, row in df_for_user.iterrows():
#         news_id = int(row['news_id'])
#         title = row['title']
#         date = str(row['date_time'])
#         obj['history'].append(
#             {
#                 'id': news_id,
#                 'title': title,
#                 'date': date
#             }
#         )
#     result.append(obj)
#
# with open('data/history.json', 'w', encoding='utf-8') as f:
#     json.dump(result, f, ensure_ascii=False,  indent=4)



# {'user_id': [
#     {
#         'id': 'id',
#         'title': 'title',
#         'date': 'date'
#     }
# ]}


# df['news_type'] = df['news_id'].apply(get_news_type)

# df['news_type'].value_counts()

# news_ids_from_ds = set(df['news_id'].unique())
# news_ids_from_json = set([i.get('id') for i in data])
#
# # Тут можно посравнивать два сета и увидеть разницу в списке id
#
# df_json = pd.read_json('data/news.json', encoding="utf_8_sig")  # Закинем json в df
# df_json["news_type"] = df_json['id'].apply(get_news_type)
# df_json["news_type"].value_counts()

# with open('data/districts.json', "r", encoding="utf_8_sig") as file:
#     data_districts = json.loads(file.read())
#
# districts = list()
# for a in data_districts["items"]:
#     for d in a['areas']:
#         d['area_title'] = a['title']
#         d['area_local_id'] = a['local_id']
#         districts.append(d)
#     if not a['areas']:
#         districts.append({
#             "id": a['id'],
#             "title": a['title'],
#             "local_id": a['local_id'],
#             "district_id": None,
#             "site": None,
#             "population": None,
#             "square": None,
#             "manager_id": None,
#             "title_en": a['title_en'],
#             'area_title': a['title'],
#             'area_local_id': a['local_id']
#         })
#
# districts_df = pd.DataFrame(districts)

