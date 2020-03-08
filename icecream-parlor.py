import argparse

# --- CLI ARGS ----
parser = argparse.ArgumentParser()
parser.add_argument("--debug", type=int, help="enter debug Y/N",
                    nargs='?', default=0, const=0)
args = parser.parse_args()
debug = args.debug

# --- START SOLUTION ----

def icecreamParlor(m, arr, start = 0, debug = False):
    '''
    https://www.hackerrank.com/challenges/icecream-parlor/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
    Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.
    Return an array containing the indices of the prices of the two flavors they buy, sorted ascending.

    Parameters
    ----------
    m : int
        total budget to spend
    arr : list
        cost of each flavour

    Returns
    -------
    list
        A list of indices of the prices of the two flavors they buy, sorted ascending.
    '''

    # print(f'Max cost {m}')
    flavour_sum = 0
    flavours = []
    for flavour, cost_price in enumerate(arr, start=1):
        debug and print(f'Flavour Index: {flavour} | Cost {cost_price} | Flavour Sum {flavour_sum}')

        if cost_price >= m:
            debug and print(f'Skipping...')
            continue

        if flavour == 1:
            flavour_sum = cost_price
            flavours.append(flavour + start)
            debug and print(f'Adding first {flavour} at cost {cost_price} | flavour sum {flavour_sum}')
            continue


        if (flavour_sum + cost_price) == m and (len(flavours) == 1):
            debug and print(f'Adding next {flavour} at cost {cost_price}')
            flavours.append(flavour + start)
            break

    if len(flavours) != 2 and len(arr) > 1:
        debug and print(f'No available combos for this run, popping and recalling...')
        arr.pop(0)
        start+=1
        flavours = icecreamParlor(m, arr, start, debug)

    debug and print(flavours)

    return flavours


test_cases = [
    [4, '1 4 5 3 2', '1 4'],
    [4, '2 2 4 3', '1 2'],
    [9, '1 3 4 6 7 9', '2 4'],
    [8, '1 3 4 4 6 8', '3 4'],
    [3 , '1 2', '1 2']
]

for test_case in test_cases:
    budget = test_case[0]
    flavours = [int(x) for x in test_case[1].split()]
    result = [int(x) for x in test_case[2].split()]
    start = 0

    print(f'Case: Budget {budget} | Flavours {flavours} | Expected {result}\n-----------------------')
    print(f'Success: {icecreamParlor(budget, flavours, start, debug) == result}\n-----------------------')

# help(icecreamParlor)