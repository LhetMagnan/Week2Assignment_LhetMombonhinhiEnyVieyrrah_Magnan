import numpy as np

def max_profit(objects, profits, weights, max_w):
    np_objects = np.array(objects)
    np_profits = np.array(profits)
    np_weights = np.array(weights)
    fraction = np_profits / np_weights

    fraction_dict = {}
    j = 0
    for i in fraction:
        fraction_dict[i] = j
        j += 1

    fraction_tuple = sorted(fraction_dict.items())
    selected_fractions = []
    selected_profit = []
    selected_objects = []

    while (max_w > 0):
        i = len(fraction_tuple) - 1
        while (i >= 0):
            if (max_w >= np_weights[fraction_tuple[i][1]]):
                max_w -= np_weights[fraction_tuple[i][1]]
                selected_fractions.append(1)
                selected_profit.append(np_profits[fraction_tuple[i][1]])
                selected_objects.append(np_objects[fraction_tuple[i][1]])

            elif (max_w <= np_weights[fraction_tuple[i][1]]):
                temp = max_w
                max_w -= max_w
                selected_fractions.append(temp / weights[fraction_tuple[i][1]])
                selected_profit.append(np_profits[fraction_tuple[i][1]])
                selected_objects.append(np_objects[fraction_tuple[i][1]])

                break

            i -= 1

    while(len(selected_fractions) != len(np_weights)):
        selected_fractions.append(0)
        selected_profit.append(0)
    #          Calculate the total profit
    array_total_profit = np.array(selected_fractions)*(np.array(selected_profit))
    total_profit = array_total_profit.sum()
    return selected_objects, selected_fractions, total_profit