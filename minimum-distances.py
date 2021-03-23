
import argparse

# --- CLI ARGS ----
parser = argparse.ArgumentParser()
parser.add_argument("--debug", type=int, help="enter debug Y/N", nargs='?', default=0, const=1)
parser.add_argument("--annotate", type=int, help="enter for python def help Y/N", nargs='?', default=0, const=1)
args = parser.parse_args()

debug = args.debug
annotate = args.annotate

# --- START SOLUTION ----
def minimumDistances(a):
    '''
    https://www.hackerrank.com/challenges/minimum-distances/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
    The distance between two array values is the number of indices between them. Given , find the minimum distance between any pair of equal elements in the array. If no such value exists, return -1
    :param a: list
    return: int
    '''

    global debug
    diff = -1

    counts = {x: a.count(x) for x in a if a.count(x) == 2}

    if 2 not in counts.values():
        debug and print(f'Counts {counts}')
        return diff

    element_diff = 0
    for key, value in counts.items():
        debug and print(f'{key} {value}')
        indices = [x for x, y in enumerate(a) if y == key]
        debug and print(indices)
        current_diff = indices[1] - indices[0]
        debug and print(f'current_diff {current_diff}')

        if element_diff == 0 or current_diff < element_diff:
            element_diff = current_diff

    return element_diff

test_cases = [
    ['1 2', -1],
    ['3 2 1 2 3', 2],
    ['7 1 3 4 1 7', 3],
]

for test_case in test_cases:
    a = [int(x) for x in test_case[0].split()]
    result = minimumDistances(a)
    passed = '\033[1;32mTrue\033[0m' if result == test_case[1] else '\033[1;31mFalse\033[0m'
    print(f'Case: number of elements {len(a)} | [n] {a} | Expected {test_case[1]} | Result {result}')
    print(f'Success: {passed}\n------------------')


if annotate:
    help(minimumDistances)
