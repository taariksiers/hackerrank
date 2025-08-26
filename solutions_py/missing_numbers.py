from collections import Counter
from solutions_py.harness import Harness


class MissingNumbers(Harness):
    """
    https://www.hackerrank.com/challenges/missing-numbers/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
    While transporting them from one exhibition to another, some numbers were lost out of the first list. Can you find the missing numbers?
    """

    def solution(self, arr: list, brr: list) -> int:
        """
        :param arr: list
        :param brr: list
        :return: int
        """
        debug, a_count, b_count, elem_diff = self.debug, Counter(arr), Counter(brr), list()
        debug and print(f'Diff {a_count} {b_count}')

        if a_count == b_count:
            return elem_diff

        for num, occurrences in b_count.items():

            a_occurrences = a_count[num] is None and 0 or a_count[num]

            if occurrences > a_occurrences:
                elem_diff.append(num)

        if len(elem_diff) > 1:
            elem_diff.sort()

        return elem_diff

    @staticmethod
    def _test_cases() -> list:
        """
        Format: dictionary item with 'kwargs' for inputs
        :return: list
        """
        return [
            {'kwargs': {'arr': [7, 2, 5, 3, 5, 3], 'brr': [7, 2, 5, 4, 6, 3, 5, 3]}, 'expected': [4, 6]},
            {'kwargs': {'arr': [203, 204, 205, 206, 207, 208, 203, 204, 205, 206],
                        'brr': [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]},
             'expected': [204, 205, 206]}
        ]
