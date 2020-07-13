import numpy as np


def hit_rate(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    hit_rate = (flags.sum() > 0) * 1

    return hit_rate


def hit_rate_at_k(recommended_list, bought_list, k):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])

    flags = np.isin(bought_list, recommended_list)

    hit_rate = (flags.sum() > 0) * 1

    return hit_rate


def recall(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)  # [False, False, True, True]

    recall = flags.sum() / len(bought_list)

    return recall


def recall_at_k(recommended_list, bought_list, k):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])

    flags = np.isin(bought_list, recommended_list)

    recall = flags.sum() / len(bought_list)

    return recall


# решение через цикл
def money_recall_at_k(recommended_list, bought_list, prices_recommended, prices_bought, k):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])
    prices_recommended = np.array(prices_recommended[:k])
    prices_bought = np.array(prices_bought)

    sum_bought = 0
    for i in range(len(bought_list)):
        if bought_list[i] in recommended_list:
            sum_bought += prices_bought[i]

    recall = sum_bought / prices_bought.sum()

    return recall


# решение через скалярное произведение
def money_recall_at_k_2(recommended_list, bought_list, prices_recommended, prices_bought, k):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])
    prices_recommended = np.array(prices_recommended[:k])
    prices_bought = np.array(prices_bought)

    flags = np.isin(bought_list, recommended_list)
    sum_bought = np.dot(flags, prices_bought)

    recall = sum_bought / prices_bought.sum()

    return recall


def ap_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(recommended_list, bought_list)

    if sum(flags) == 0:
        return 0

    sum_ = 0
    for i in range(1, k + 1):

        if flags[i] == True:
            p_k = precision_at_k(recommended_list, bought_list, k=i)
            sum_ += p_k

    result = sum_ / sum(flags)

    return result


def map_k(recommended_list, bought_list, k=5):
    # your_code

    return result

def reciprocal_rank(recommended_list, bought_list):
    # your_code
    return result


def precision_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def money_precision_at_k_2(recommended_list, bought_list, prices_recommended, prices_bought, k):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])
    prices_recommended = np.array(prices_recommended[:k])

    flags = np.isin(bought_list, recommended_list)
    sum_bought = np.dot(flags, prices_bought)

    precision = sum_bought / prices_recommended.sum()

    return precision


def money_precision_at_k(recommended_list, bought_list, prices_recommended, k):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])
    prices_recommended = np.array(prices_recommended[:k])

    sum_bought = 0
    for i in range(len(recommended_list)):
        if recommended_list[i] in bought_list:
            sum_bought += prices_recommended[i]

    precision = sum_bought / prices_recommended.sum()

    return precision


