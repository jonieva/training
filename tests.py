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


def condense_meeting_times(times, return_in_minutes=False):
    """ Your company built an in-house calendar tool called HiCal.
    You want to add a feature to see the times in a day when everyone is available.
    """
    # Reserve space for 15 hours (2 half-hours per hour)
    l = 30
    result = [False]*l

    for t in times:
        # Get all the intervals and add them to the list of scheduled times
        start = t[0]
        end = t[1]
        while start < end:
            result[start] = True
            start += 1
    # Condense the hours
    condensed_result = []
    start = -1
    for h in range(l):
        if result[h]:
            # Found first element
            start = h
            break
    if start == -1:
        # Not hours found
        return []

    # start and h contain the first index, we have to find the last
    h = start + 1
    meeting_going_on = True
    while h < l:
        if result[h]:
            # Meeting still on. Nothing
            meeting_going_on = True
            if start == -1:
                start = h
        elif meeting_going_on:
            # Stop
            condensed_result.append((start, h))
            meeting_going_on = False
            start = -1
        h += 1
    # print condensed_result
    condensed_result_modified = []
    if return_in_minutes:
        offset = 9*60
        for t in condensed_result:
            condensed_result_modified.append((t[0]+offset, t[1]*30+offset))
        return condensed_result_modified
    else:
        return condensed_result
#times =   [(1, 10), (2, 6), (3, 5), (7, 9), (11,12)]


def denominations(amount, denoms):
    """ Write a function that, given:
        an amount of money
        a list of coin denominations
        computes the number of ways to make amount of money with coins of the available denominations.
    :param amount:
    :param denoms:
    :return:
    """
    results = []
    __denominations_rec__(amount, denoms, [], results)
    return results

def __denominations_rec__(amount, denoms, partial_sol, solutions):
    acc = sum(partial_sol)
    print("partial_sol: {0}, solutions: {1}".format(partial_sol, solutions))
    if acc == amount:
        solutions.append(list(partial_sol))
    elif acc < amount:
        for d in denoms:
            p = list(partial_sol)
            p.append(d)
            __denominations_rec__(amount, denoms, p, solutions)
    return acc

def denominations2(amount, my_denoms):
    final_sols = list()
    for i in range(amount + 1):
        final_sols.append(list())

    candidates_to_review = list()
    for denom in my_denoms:
        # Add this denom to all the possible solutions that lead to this number
        if denom < amount:
            final_sols[denom].append([denom])
            candidates_to_review.append(denom)

    print ("Initial candidates:", candidates_to_review)
    print ("Initial sols:", final_sols)
    while len(candidates_to_review) > 0:
        # Extract first element to avoid duplicated results
        candidates_to_review.sort()
        index = candidates_to_review.pop(0)
        print ("Index reviewed: ", index)
        previous_solutions = final_sols[index]
        for denom in my_denoms:
            s = index + denom
            if s <= amount:
                # Add this denom to all the posibilities that we had to arrive to this candidate
                for prev_sol in previous_solutions:
                    # Copy list
                    prev_sol = list(prev_sol)
                    # Add the new denom
                    prev_sol.extend([denom])
                    final_sols[s].append(prev_sol)
                    if s < amount and s not in candidates_to_review:
                        candidates_to_review.append(s)
                print ("Candidates:", candidates_to_review)
                print ("Sols:", final_sols)

    print ("Final: ", final_sols)
    return final_sols[10]


# print ("result: ", denominations2(10, [2,4]))

def bounding_boxes(b1, b2):
    if b1['bottom_y'] < b2['bottom_y']:
        bottom_y = b1
        top_y = b2
    else:
        bottom_y = b2
        top_y = b1

    if b1['left_x'] < b2['left_x']:
        left_x = b1
        right_x = b2
    else:
        left_x = b2
        right_x = b1

    # Check for wrong cases
    # No intersection
    if bottom_y['bottom_y'] + bottom_y["height"] < top_y['bottom_y'] or \
        left_x["left_x"] + left_x["width"] < right_x["left_x"]:
        return None

    # One rectangle totally contained inside another
    if top_y['bottom_y'] + top_y["height"] < bottom_y['bottom_y'] + bottom_y['height'] and \
        right_x["left_x"] + right_x["width"] < left_x["left_x"] + left_x["width"]:
        return right_x


    # Calculate coords
    lx = right_x["left_x"]
    width = left_x["left_x"] + left_x["width"] - right_x["left_x"]
    by = top_y["bottom_y"]
    height = bottom_y["bottom_y"] + bottom_y["height"] - top_y["bottom_y"]
    return {
        'left_x': lx,
        'bottom_y': by,
        # width and height
        'width': width,
        'height': height,
    }

b1 = {
    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,
    # width and height
    'width': 10,
    'height': 4,
}

b11 = {
    # coordinates of bottom-left corner
    'left_x': 11,
    'bottom_y': 6,
    # width and height
    'width': 3,
    'height': 4,
}

b2 = {
    # coordinates of bottom-left corner
    'left_x': 3,
    'bottom_y': 6,
    # width and height
    'width': 10,
    'height': 8,
}

print (bounding_boxes(b1, b11))

class TempTracker(object):
    max_ = min_ = mode_ = __most_frequent__ = _sum = _mean = None
    mode_dict = dict()
    __lenght__ = 0

    def insert_measure(self, temp):
        temp = int(round(temp, 0))
        if temp > self.max_: self.max_ = temp
        elif temp < self.min_: self.min_ = temp
        self.__lenght__ += 1
        self.sum_ += temp
        self.mean_ = (float)self.sum_ / self.__lenght__
        self.mode_dict[temp] = 1 if not self.mode_dict.has_key(temp) else self.mode_dict[temp] + 1
        if self.mode_dict[temp] > self.__most_frequent__:
            self.mode_ = temp
            self.__most_frequent__ = self.mode_dict[temp]

    def get_mean(self):
        return self.mean_