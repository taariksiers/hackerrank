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

def quickSort(arr):
    '''
    https://www.hackerrank.com/challenges/quicksort1/problem
    Quick sort 1
    :param arr: list
    :return: list
    '''

    global debug

    if len(arr) == 1:
        print(" ".join([str(x) for x in arr]))
        return arr

    pivot = arr[0]
    left = list()
    right = list()

    for index, num in enumerate(arr):

        debug and print(f'index {index} num {num}')

        if pivot < num:
            right.append(num)
            continue

        if pivot > num:
            left.append(num)
            continue

    print(f'{" ".join([str(x) for x in left])} {pivot} {" ".join([str(x) for x in right])}')

    debug and print('-----------------------------')
    return left + [pivot] + right



test_cases = [
    ['5 7 4 3 8', '4 3 5 7 8'],
    ['4 5 3 7 2', '3 2 4 5 7']
]

for test_case in test_cases:
    arr = [int(x) for x in test_case[0].split()]
    expected = [int(y) for y in test_case[1].split()]

    print(f'Case: number of elements {len(arr)} | Unsorted {arr} | Expected {expected}')
    print(f'Success: {quickSort(arr) == expected}\n------------------')


if annotate:
    help(quickSort)