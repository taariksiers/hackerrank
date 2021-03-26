import argparse

# --- CLI ARGS ----
parser = argparse.ArgumentParser()
parser.add_argument("--debug", type=int, help="enter debug Y/N",
                    nargs='?', default=0, const=0)
args = parser.parse_args()
debug = args.debug

# --- START SOLUTION ----

def insertionSort1(n, arr):
    '''
    https://www.hackerrank.com/challenges/insertionsort1/problem?h_r=internal-search
    One common task for computers is to sort data. For example, people might want to see all their files on a computer sorted by size.
    Since sorting is a simple problem with many different possible solutions, it is often used to introduce the study of algorithms.
    Parameters
    ----------
    n : int
        number of elements
    arr: list
        partially sorted list

    Returns
    -------
    list
        A list of indices of the prices of the two flavors they buy, sorted ascending.
    '''

    global debug

    last_num = arr[-1]

    debug and print(f'last_num {last_num}')
    last_set = False

    for index in range(len(arr)-2, -1, -1): # reverse loop through array with index start from 2nd last element
        current_num = arr[index]
        if current_num > last_num:
            debug and print(f'Setting index {index+1} to current_num {current_num}')
            arr[index+1] = current_num
        else:
            debug and print(f'ELSE index {index+1} to last_num {last_num}')
            arr[index+1] = last_num
            last_set = True

        print(' '.join([str(x) for x in arr]))

        if last_set:
            break

    # if we never end up setting the number then this must be the lowest number
    if last_set == False:
        arr[0] = last_num
        print(' '.join([str(x) for x in arr]))

    return arr

test_cases = [
    ['2 4 6 8 3', '2 3 4 6 8'],
    ['1 2 4 5 3', '1 2 3 4 5'],
    ['2 3 4 5 6 7 8 9 10 1', '1 2 3 4 5 6 7 8 9 10']
]

for test_case in test_cases:
    arr = [int(x) for x in test_case[0].split()]
    expected = [int(y) for y in test_case[1].split()]

    print(f'Case: number of elements {len(arr)} | List partially sorted {arr} | Expected {expected}')
    print(f'Success: {insertionSort1(len(arr), arr) == expected}\n------------------')

# help(insertionSort1)