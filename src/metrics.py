import numpy as np


def precision(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def precision_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    

    bought_list = bought_list  # Тут нет [:k] !!
    
    if k < len(recommended_list):
        recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def money_precision_at_k_1(recommended_list, bought_list, price_item, k=5):
    
    recommended_list = recommended_list[:k]
    prices_recommended = []
    for n in range(len(recommended_list)):
        a = price_item.loc[price_item.index == recommended_list[n]]
        prices_recommended.append(a[recommended_list[n]])
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    prices_recommended = np.array(prices_recommended)
    
    sum_bought = 0
    for i in range (len(recommended_list)):
        if recommended_list[i] in bought_list:
            sum_bought += prices_recommended[i]
    
    precision = sum_bought / prices_recommended.sum()
    
    return precision  


# решение через скалярное произведение. но пришлось добавить переменную prices_bought...
def money_precision_at_k(recommended_list, bought_list, prices_recommended, prices_bought, k):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])
    prices_recommended = np.array(prices_recommended[:k])
    
    flags = np.isin(bought_list, recommended_list)
    sum_bought=np.dot(flags,prices_bought)
    
    precision = sum_bought / prices_recommended.sum()
    
    return precision 


def recall(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    recall = flags.sum() / len(bought_list)

    return recall


def recall_at_k(recommended_list, bought_list, k=5):

    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    if k < len(recommended_list):
        recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)
    recall = flags.sum() / len(bought_list)

    return recall


# решение через цикл    
def money_recall_at_k_1(recommended_list, bought_list, prices_recommended, prices_bought, k):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])
    prices_recommended = np.array(prices_recommended[:k])
    prices_bought =np.array(prices_bought)
    
    sum_bought=0
    for i in range (len(bought_list)):
        if bought_list[i] in recommended_list:
            sum_bought += prices_bought[i]
    
    recall = sum_bought / prices_bought.sum()
    
    return recall


# решение через скалярное произведение
def money_recall_at_k(recommended_list, bought_list, prices_recommended, prices_bought, k):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])
    prices_recommended = np.array(prices_recommended[:k])
    prices_bought =np.array(prices_bought)
    
    flags = np.isin(bought_list, recommended_list)
    sum_bought=np.dot(flags,prices_bought)
    
    recall = sum_bought / prices_bought.sum()
    
    return recall