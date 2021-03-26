import argparse

# --- CLI ARGS ----
parser = argparse.ArgumentParser()
parser.add_argument("--debug", type=int, help="enter debug Y/N", nargs='?', default=0, const=0)
parser.add_argument("--annotate", type=int, help="enter for python def help Y/N", nargs='?', default=0, const=1)
args = parser.parse_args()

debug = args.debug
annotate = args.annotate

# --- START SOLUTION ----

def balancedSums(arr):
    '''
    https://www.hackerrank.com/challenges/sherlock-and-array/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
    Watson gives Sherlock an array of integers.
    His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.
    :param arr: list
    :return: bool
    '''

    global debug

    if len(arr) == 1:
        return 'YES'

    if len(arr) == 3:
        return arr[0] == arr[-1] and 'YES' or 'NO'

    balanced = False
    last_num = None
    total_sum = sum(arr)
    right = total_sum - arr[0]

    for index, num in enumerate(arr):

        if index == 0:
            left = 0
        else:
            right = total_sum - left
            left += last_num

        last_num = num

        debug and print(f'DEBUG | index {index} | num {num} | LEFT {left} | RIGHT {right}')
        if left == right:
            balanced = True
            break

    debug and print(f'DEBUG | Balanced {balanced}')
    return balanced and 'YES' or 'NO'


test_cases = [
    ['1 2 3', 'NO'],
    ['1 2 3 3', 'YES'],
    ['5 6 8 11', 'YES'],
    ['2 0 0 0', 'YES']
]

for test_case in test_cases:
    arr = [int(x) for x in test_case[0].split()]

    print(f'Case: number of elements {len(arr)} | [n] {arr} | Expected {test_case[1]}')
    print(f'Success: {balancedSums(arr) == test_case[1]}\n------------------')


if annotate:
    help(balancedSums)