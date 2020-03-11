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

def insertionSort2(n, arr):
    '''
    https://www.hackerrank.com/challenges/insertionsort2/problem
    Insertion sort part deux
    :param n: int
    :param arr: list
    :return: list
    '''

    global debug

    if len(arr) == 1:
        print(" ".join([str(x) for x in arr]))
        return arr

    for index in range(len(arr)):

        current_num = arr[index]

        next_num = (index != len(arr) - 1) and arr[index+1] or None

        debug and print(f'INDEX [{index}] | CANDIDATE {current_num} | COMPARE {next_num}')

        if next_num is None:
            break

        if current_num < next_num:
            print(" ".join([str(x) for x in arr]))
            debug and print('-----------------------------')
            continue

        debug and print(f'SWAP | Standard num swap')
        arr[index] = next_num
        arr[index+1] = current_num

        candidate = next_num

        for reindex in range(len(arr[0:index]), -1, -1):

            debug and print(f'REVERSING | current_num {current_num} | reindex {reindex} | current_reindex_num {arr[reindex]} | previous_num {arr[reindex-1]}')
            current_reindex_num = arr[reindex]

            if candidate < current_reindex_num:
                debug and print(f'Swapping reverse nums')
                arr[reindex] = candidate
                arr[reindex+1] = current_reindex_num


        print(" ".join([str(x) for x in arr]))

    debug and print('-----------------------------')
    return arr



test_cases = [
    ['2 4 6 8 3', '2 3 4 6 8'],
    ['1 2 4 5 3', '1 2 3 4 5'],
    ['2 3 4 5 6 7 8 9 10 1', '1 2 3 4 5 6 7 8 9 10'],
    ['3 4 7 5 6 2 1', '1 2 3 4 5 6 7'],
    ['1 4 3 5 6 2', '1 2 3 4 5 6']
]

for test_case in test_cases:
    arr = [int(x) for x in test_case[0].split()]
    expected = [int(y) for y in test_case[1].split()]

    print(f'Case: number of elements {len(arr)} | Unsorted {arr} | Expected {expected}')
    print(f'Success: {insertionSort2(len(arr), arr) == expected}\n------------------')


if annotate:
    help(insertionSort2)