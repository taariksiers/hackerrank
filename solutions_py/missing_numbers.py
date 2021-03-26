from collections import Counter
import argparse

# --- CLI ARGS ----
parser = argparse.ArgumentParser()
parser.add_argument("--debug", type=int, help="enter debug Y/N",
                    nargs='?', default=0, const=0)
parser.add_argument("--annotate", type=int, help="enter for python def help Y/N",
                    nargs='?', default=0, const=0)
args = parser.parse_args()

debug = args.debug
annotate = args.annotate

# --- START SOLUTION ----

def missingNumbers(arr, brr):
    '''
    https://www.hackerrank.com/challenges/missing-numbers/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
    While transporting them from one exhibition to another, some numbers were lost out of the first list. Can you find the missing numbers?
    :param arr: list
    :param brr: list
    :return: list
    '''

    global debug

    bCount = Counter(brr)
    aCount = Counter(arr)
    elem_diff = list()

    debug and print(f'Diff {bCount} {aCount}')

    if bCount == aCount:
        return elem_diff

    for num, occurrences in bCount.items():

        a_occurences = aCount[num] is None and 0 or aCount[num]

        if occurrences > a_occurences:
            elem_diff.append(num)

    if len(elem_diff) > 1:
        elem_diff.sort()

    return elem_diff



test_cases = [
    ['7 2 5 3 5 3', '7 2 5 4 6 3 5 3', '4 6'],
    ['203 204 205 206 207 208 203 204 205 206', '203 204 204 205 206 207 205 208 203 206 205 206 204', '204 205 206']
]

for test_case in test_cases:
    arr = [int(x) for x in test_case[0].split()]
    brr = [int(x) for x in test_case[1].split()]
    expected = [int(y) for y in test_case[2].split()]

    print(f'Case: number of elements {len(arr)} | Arg 1 {arr}  Arg 2 {brr} | Expected {expected}')
    print(f'Success: {missingNumbers(arr, brr) == expected}\n------------------')


if annotate:
    help(missingNumbers)