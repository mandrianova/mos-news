import os
import pickle

import pandas as pd
import numpy as np
import json
from scipy.sparse import csr_matrix
from implicit.nearest_neighbours import ItemItemRecommender


pd.set_option('display.max_columns', None)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_to_data_folder = os.path.join(BASE_DIR, 'data')

source_json = os.path.join(path_to_data_folder, 'news.json')
source_xlsx = os.path.join(path_to_data_folder, 'dataset_news_1.xlsx')

source_data_recom_dir = os.path.join(path_to_data_folder, 'data_recommendation')
source_to_model = os.path.join(source_data_recom_dir, 'model.pickle')
source_to_final_df = os.path.join(source_data_recom_dir, 'final_df.pickle')
source_to_user_ids = os.path.join(source_data_recom_dir, 'user_ids.pickle')
source_to_news_ids = os.path.join(source_data_recom_dir, 'news_ids.pickle')
source_to_csr_matrix = os.path.join(source_data_recom_dir, 'csr_matrix.pickle')


def retrain_recommend_model():
    with open(source_json, "r", encoding="utf_8_sig") as news_json:
        data = json.loads(news_json.read())

    news_types = set()

    for i in data:
        news_types.add(str(i.get('id'))[-3:])

    df = pd.read_excel(source_xlsx)

    def get_news_id_from_url(url: str) -> int:
        parts = url.split('/')
        try:
            if parts[-2] == '9468':
                print(url)
            return int(parts[-2])
        except Exception as err:
            print(url)
            for part in parts:
                if '073' in part:
                    return int(part)
            print("it is not news url ", url)
            return 0

    def get_news_type(news_id: int) -> str:
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

    df_json = pd.read_json(source_json, encoding="utf_8_sig")  # Закинем json в df
    df_json["news_type"] = df_json['id'].apply(get_news_type)
    df_json["news_type"].value_counts()

    merged = df.merge(df_json,
                      left_on='news_id',
                      right_on='id')

    show_difference = pd.to_datetime(merged['date_time']).sub(merged['published_at'])
    days = show_difference.dt.days
    merged['published/read'] = days

    final_df = merged.drop(['importance', 'is_deferred_publication', 'status', 'ya_rss', 'active_from',
                            'active_to', 'search', 'display_image', 'icon_id', 'canonical_url', 'canonical_updated_at',
                            'is_powered', 'has_image', 'attach', 'active_from_timestamp', 'active_to_timestamp',
                            'image', 'counter', 'preview_text', 'images'],
                           axis=1)
    final_df['sphere_id'] = final_df.sphere.map(lambda row: row.get('id'))
    final_df['title_age'] = (final_df['published_at'].max() - final_df['published_at']).dt.days + 1
    final_df['age_param'] = 1 / final_df['title_age']
    final_df['date_time'].dt.day.min()
    final_df = final_df[['user_id', 'news_id', 'date_time', 'age_param', 'title', 'published_at']]

    result = final_df.groupby('user_id')['news_id'].unique().reset_index()
    result.columns = ['user_id', 'actual']
    result['actual'] = result['actual'].apply(lambda x: list(x))

    popularity = final_df['news_id'].value_counts().reset_index()
    popularity.columns = ['news_id', 'count']
    recs_pop = list(popularity.head(7).news_id)
    result['popular_recommendation'] = result['user_id'].apply(lambda x: recs_pop)

    user_item_matrix = pd.pivot_table(final_df,
                                      index='user_id', columns='news_id',
                                      values='age_param',
                                      fill_value=0
                                      )

    user_item_matrix = user_item_matrix.astype(float)

    sparse_user_item = csr_matrix(user_item_matrix).T

    user_item_matrix.head(5)

    model = ItemItemRecommender(K=6)
    model.fit(sparse_user_item, show_progress=False)

    user_ids = list(user_item_matrix.index.values)
    news_ids = list(user_item_matrix.columns.values)

    with open(source_to_model, 'wb') as f:
        pickle.dump(model, f)
    with open(source_to_final_df, 'wb') as f:
        pickle.dump(final_df, f)
    with open(source_to_user_ids, 'wb') as f:
        pickle.dump(user_ids, f)
    with open(source_to_news_ids, 'wb') as f:
        pickle.dump(news_ids, f)
    with open(source_to_csr_matrix, 'wb') as f:
        pickle.dump(sparse_user_item, f)


def recommend_user(user_id, model, sparse_user_item, user_ids, news_ids):
    user_index = user_ids.index(user_id)
    recommendations = model.recommend(user_index, sparse_user_item, N=20)

    result = [news_ids[x[0]] for x in recommendations]
    return result


def generate_recommendations(user_id):
    with open(source_to_csr_matrix, 'rb') as f:
        sparse_user_item = pickle.load(f)
    with open(source_to_model, 'rb') as f:
        model = pickle.load(f)
    with open(source_to_user_ids, 'rb') as f:
        user_ids = pickle.load(f)
    with open(source_to_news_ids, 'rb') as f:
        news_ids = pickle.load(f)
    with open(source_to_final_df, 'rb') as f:
        df = pickle.load(f)
    recs_list = []
    for news_id in recommend_user(user_id, model, sparse_user_item, user_ids, news_ids):
        recommended_news = {'id': news_id,
                            'title': str(list(df.loc[(df['news_id'] == news_id)]['title'])[0]),
                            'date': str(list(df.loc[(df['news_id'] == news_id)]['published_at'])[0])}
        recs_list.append(recommended_news)

    return recs_list


def generate_csv_file():
    with open(source_to_csr_matrix, 'rb') as f:
        sparse_user_item = pickle.load(f)
    with open(source_to_model, 'rb') as f:
        model = pickle.load(f)
    with open(source_to_user_ids, 'rb') as f:
        user_ids = pickle.load(f)
    with open(source_to_news_ids, 'rb') as f:
        news_ids = pickle.load(f)

    recs_list = []
    for user_id in user_ids:
        rec = recommend_user(user_id, model, sparse_user_item, user_ids, news_ids)[:5]
        new_lst = [user_id, *rec]
        recs_list.append(new_lst)
        df = pd.DataFrame(data=recs_list,
                          columns=['user_id', 'news_id_1', 'news_id_2', 'news_id_3', 'news_id_4', 'news_id_5'])
        df.to_csv('result_task10.csv', index=False)
