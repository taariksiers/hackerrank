from solutions_py.harness import Harness


class SherlockAndArray(Harness):
    """
    https://www.hackerrank.com/challenges/sherlock-and-array/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
    Watson gives Sherlock an array of integers.
    His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum
    of all elements to the right.
    """

    def solution(self, arr: list) -> str:
        """
        :param arr: list
        :return: str
        """
        debug = self.debug

        if len(arr) == 1:
            return 'YES'

        if len(arr) == 3:
            return 'YES' if arr[0] == arr[-1] else 'NO'

        balanced, last_num, total_sum = False, None, sum(arr)
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
        return 'YES' if balanced else 'NO'

    @staticmethod
    def _test_cases() -> list:
        """
        Format: dictionary item with 'kwargs' for inputs, 'result' for expected output
        :return: list
        """
        return [
            {'kwargs': {'arr': [1, 2, 3]}, 'result': 'NO'},
            {'kwargs': {'arr': [1, 2, 3, 3]}, 'result': 'YES'},
            {'kwargs': {'arr': [5, 6, 8, 11]}, 'result': 'YES'},
            {'kwargs': {'arr': [2, 0, 0, 0]}, 'result': 'YES'}
        ]
