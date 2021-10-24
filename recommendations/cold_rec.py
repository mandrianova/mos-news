import os
import json
import pickle

import pandas as pd

from auto_markup.support_for_model.support_decorators import try_except_none_wrapper

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

path_to_history = os.path.join(BASE_DIR, 'data', 'dataset_news_1.xlsx')
path_to_news = os.path.join(BASE_DIR, 'data', 'news.json')
path_to_districts = os.path.join(BASE_DIR, 'data', 'districts.json')
path_to_combined_data = os.path.join(BASE_DIR, 'data', 'data_cold_recommendation', 'combined_data.json')
path_to_cold_recommendations = os.path.join(BASE_DIR, 'data', 'data_cold_recommendation', 'cold_recommendations.pickle')
key_fields = ['id', 'created_at', 'published_at', 'status', 'kind', 'title', 'preview_text',
              'tags', 'url', 'sphere', 'spheres', 'label', 'area_title', 'district_title']


def combine_data():
    dataset = pd.read_excel(path_to_history)
    dataset['news_id'] = [int(str(i[-1]).strip()) for i in dataset.url_clean.str.findall(r"(\d{4,})")]
    dataset.news_id.fillna(0, inplace=True)
    df_news = pd.read_json(path_to_news)
    string_columns = df_news.select_dtypes('object').columns
    val_columns = df_news.select_dtypes(exclude='object').columns
    df_news[string_columns] = df_news[string_columns].fillna('')
    df_news[val_columns] = df_news[val_columns].fillna(0)
    df_news[['preview_text', 'full_text']] = df_news[['preview_text', 'full_text']].fillna('')
    df_news.preview_text = df_news.apply(lambda c: c.preview if len(c.preview) > 0 else c.preview_text, axis=1)
    df_news.full_text = df_news.apply(lambda c: c.text if len(c.text) > 0 else c.full_text, axis=1)
    with open(os.path.join(BASE_DIR, 'data', 'districts.json'), 'r') as file:
        districts = json.load(file)['items']
    distr = pd.DataFrame(districts)
    frames = [pd.DataFrame(i) for i in distr.areas]
    areas = pd.concat(frames)
    areas_full = areas.merge(distr[['id', 'title']], left_on='district_id', right_on='id', how='left', copy=False)
    areas_full.rename(columns={'id_x': 'area_id', 'title_x': 'area_title', 'title_y': 'district_title'}, inplace=True)
    df_news = df_news.merge(areas_full[['area_id', 'area_title', 'district_title']], left_on='territory_area_id',
                            right_on='area_id', how='left')
    df_mod = df_news[key_fields]
    df_fin = pd.merge(dataset, df_mod, left_on='news_id', right_on='id', how='left')
    df_fin.drop(df_fin[df_fin.created_at.isna()].index, inplace=True)
    df_fin['kind'] = df_fin.kind.apply(lambda s: s.get('title', ''))
    df_fin['sphere'] = df_fin.sphere.apply(lambda s: s.get('title', ''))
    df_fin['spheres'] = df_fin.spheres.apply(lambda s: [i.get('title', '') for i in s])
    df_fin['tags'] = df_fin.tags.apply(lambda s: [i.get('title', '') for i in s])
    df_fin.drop(columns=['id'], inplace=True)
    date_time_cols = ['date_time', 'created_at', 'published_at']
    df_fin[date_time_cols] = df_fin[date_time_cols].apply(lambda col: pd.to_datetime(col))
    df_fin['marker'] = [1 for i in range(df_fin.shape[0])]
    df_fin['time_alive'] = df_fin.date_time - df_fin.published_at
    df_fin['days_alive'] = df_fin.time_alive.apply(lambda d: d.days)
    df_fin['hours_alive'] = df_fin.time_alive.apply(lambda d: d.components.hours)
    # df_fin.drop(columns=['url']).to_json(path_to_combined_data, orient='records', force_ascii=False)
    return df_fin


def update_cold_recommendations():
    df = combine_data()
    df.sort_values(by='time_alive', inplace=True)
    df['n_views'] = df.groupby('news_id')['marker'].cumsum()
    median_views = df.n_views.median()

    def get_rank(n_views, days_alive):
        if days_alive == 0:
            days_alive += 1
        if n_views < median_views:
            n_views = median_views
        return n_views / days_alive

    df['rank'] = df.apply(lambda x: get_rank(x.n_views, x.days_alive), axis=1)
    rating = df[['news_id', 'title', 'published_at', 'n_views', 'days_alive', 'rank']].drop_duplicates(
        subset='news_id').sort_values(by='rank', ascending=False)
    rating.rename(columns={'news_id': 'id', 'published_at': 'date'}, inplace=True)
    rating['date'] = rating.date.apply(lambda d: pd.to_datetime(d).strftime(format='%Y-%m-%d %H:%M'))

    lst_of_cold_recommendations = []
    n = 0

    for index, row in rating[['id', 'title', 'date']].iterrows():
        n += 1
        obj = {
            'id': row['id'],
            'title': row['title'],
            'date': row['date'],
        }
        lst_of_cold_recommendations.append(obj)
        if n >= 20:
            break

    with open(path_to_cold_recommendations, 'wb') as f:
        pickle.dump(lst_of_cold_recommendations, f)


@try_except_none_wrapper
def get_cold_recommendations():
    with open(path_to_cold_recommendations, 'rb') as f:
        lst_of_cold_recommendations = pickle.load(f)
    return lst_of_cold_recommendations
