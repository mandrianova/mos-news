import os
import json
import time
import threading
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WAIT_SECONDS = 60*60*24

ticker = threading.Event()

path_to_history = os.path.join(BASE_DIR, 'data', 'dataset_news_1.xlsx')
path_to_news = os.path.join(BASE_DIR, 'data', 'news.json')
path_to_districts = os.path.join(BASE_DIR, 'data', 'districts.json')
path_to_combined_data = os.path.join(BASE_DIR, 'data', 'combined_data.json')
key_fields = ['id', 'created_at', 'published_at', 'status', 'kind', 'title', 'preview_text', 'tags', 'url', 'sphere', 'spheres', 'label', 'area_title', 'district_title']

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
    df_news = df_news.merge(areas_full[['area_id', 'area_title', 'district_title']], left_on='territory_area_id', right_on='area_id', how='left')
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
    df_fin.drop(columns=['url']).to_json(path_to_combined_data, orient='records', force_ascii=False)
    
    # threading.Timer(WAIT_SECONDS, combine_data).start()
    return df_fin


def get_rank(views, days_alive):
    pass


def create_cold_start_rating():
    df = pd.read_json(path_to_combined_data)
    df.sort_values(by='hours_alive', inplace=True)
    df['n_views'] = df.groupby('news_id')['marker'].cumsum()
    print(df.n_news)



# while not ticker.wait(WAIT_SECONDS):
#     combine_data()
