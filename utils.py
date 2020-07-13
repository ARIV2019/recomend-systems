import numpy as np

def prefilter_items(data, take_n_popular=5000):
    """Предфильтрация товаров"""

    # Удаление товаров, с  ценой < 2$
    data['price'] = data['sales_value'] / data['quantity']
    data = data[data['price'] > 2]

    # Удаление товаров с ценой > 40$
    data = data[data['price'] < 40]

    # Уберем товары, которые не продавались за последние 12 месяцев
    data = data[data['week_no'] > data['week_no'].max() - 12*4]
                                           
    # Уберем не интересные для рекомендации категории
                                           
    # Уберем самые популярные товары (их и так купят)
    popularity = data.groupby('item_id')['user_id'].nunique().reset_index() / data['user_id'].nunique()
    popularity.rename(columns={'user_id': 'share_unique_users'}, inplace=True)

    top_popular = popularity[popularity['share_unique_users'] > 0.7].item_id.tolist()
    data = data[~data['item_id'].isin(top_popular)]

    # Уберем самые НЕ популярные товары (их и так НЕ купят)
    top_notpopular = popularity[popularity['share_unique_users'] < 0.01].item_id.tolist()
    data = data[~data['item_id'].isin(top_notpopular)]

    #  Выбор топ-N самых популярных товаров (N = take_n_popular)
    N = take_n_popular
    popularity = data.groupby('item_id')['quantity'].sum().reset_index()
    popularity.rename(columns={'quantity': 'n_sold'}, inplace=True)
    top_N = popularity.sort_values('n_sold', ascending=False).head(N).item_id.tolist()
    data = data[data['item_id'].isin(top_N)]

    return data


def postfilter_items(user_id, recommednations):
    pass