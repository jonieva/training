stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
stock_prices_yesterday = [10, 8, 7, 6, 5, 4]


def get_max_profit(stock_prices_yesterday):
    best_buy = 0
    best_sell = 1
    max_benefit = -10000
    l = len(stock_prices_yesterday)
    for buy in range(l):
        for sell in range(buy+1, l):
            benefit =  stock_prices_yesterday[sell]-stock_prices_yesterday[buy]
            if benefit > max_benefit:
                best_buy = buy
                best_sell = sell
                max_benefit = benefit
    return best_buy, best_sell, max_benefit
#print get_max_profit(stock_prices_yesterday)

import numpy as np
integers = [0, 0, 0, 0]
def multiply(integers):
    """ For each position of a list of integers, multiply by all except the current index
    :param integers:
    :return:
    """
    # Base cases
    if len(integers) == 0:
        return 0
    if len(integers) == 1:
        return integers[0]

    integers = np.array(integers, np.int)
    l = len(integers)
    results = np.zeros(l, np.int)
    partial_results = np.zeros(l, np.int)
    partial_results[0] = integers[2:].prod()
    results[0] = partial_results[0]*integers[1]
    for i in range(1,l):
        results[i] = partial_results[i-1] * integers[i-1]
        partial_results[i] = integers[i+2:].prod() * integers[:i].prod()
    return results


def multiply3(l, num_elems):
    """
    Given a list_of_ints, find the highest_product you can get from three of the integers.
    """
    import operator
    list_pos = []
    list_neg = []

    # Get the list of the num_elems biggest numbers
    for i in range(len(l)):
        if l[i] >= 0:
            work_list = list_pos
            op = operator.le
        else:
            work_list = list_neg
            op = operator.ge

        if len(work_list) < num_elems or op(work_list[num_elems-1], l[i]):
            # Insert
            ll = len(work_list)
            j = ll - 1

            while j >= 0:
                if op(work_list[j], l[i]):
                    # Not the right position
                    j -= 1
                else:
                    # Found the position
                    break
            # Insert here
            work_list.insert(j+1, l[i])
            if ll == num_elems:
                # Extract last number
                work_list.pop()

    print list_pos, list_neg
    n = 0
    prod = 1

    while n < num_elems and (len(list_neg) >= 2 or len(list_pos) > 0):
        if len(list_neg) >= 2 and n <= num_elems-2:
            # There is option to multiply two negative numbers
            if len(list_pos) >= 2:
                # It's possible to compare two pairs
                if list_neg[0] * list_neg[1] > list_pos[0] * list_pos[1]:
                    # Take two negatives
                    prod *= list_neg[0]*list_neg[1]
                    list_neg = list_neg[2:]
                    n += 2
                else:
                    # Take two positives
                    prod *= list_pos[0]*list_pos[1]
                    list_pos = list_pos[2:]
                    n += 2
            elif len(list_pos) == 1:
                if list_neg[0] * list_neg[1] > list_pos[0]:
                    # Take two negatives
                    prod *= list_neg[0]*list_neg[1]
                    list_neg = list_neg[2:]
                    n += 2
                else:
                    # Take one positive
                    prod *= list_pos.pop(0)
                    n += 1
            else:
                # No positives, take 2 negatives
                prod *= list_neg[0]*list_neg[1]
                list_neg = list_neg[2:]
                n += 2
        else:
            # Only positives are allowed here
            prod *= list_pos.pop(0)
            n += 1

    return prod


