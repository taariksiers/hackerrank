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

def countingSort(arr):
    '''
    https://www.hackerrank.com/challenges/countingsort1/problem?h_r=next-challenge&h_v=zen
    countingSort 1
    :param arr: list
    :return: list
    '''

    global debug

    if len(arr) == 1:
        print(" ".join([str(x) for x in arr]))
        return arr

    num_counter = dict()
    for num in arr:
        if num in num_counter:
            num_counter[]



test_cases = [
    ['1 1 3 2 1', '1 1 1 2 3'],
    []
]

for test_case in test_cases:
    arr = [int(x) for x in test_case[0].split()]
    expected = [int(y) for y in test_case[1].split()]

    print(f'Case: number of elements {len(arr)} | Unsorted {arr} | Expected {expected}')
    print(f'Success: {countingSort(arr) == expected}\n------------------')


if annotate:
    help(countingSort)