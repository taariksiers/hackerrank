from solutions_py.harness import Harness


class MinimumDistances(Harness):
    """
    https://www.hackerrank.com/challenges/minimum-distances/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
    The distance between two array values is the number of indices between them. Given , find the minimum distance
    between any pair of equal elements in the array. If no such value exists, return -1
    """

    def solution(self, a) -> int:
        """
        :param a: list
        :return: int
        """
        debug, diff, element_diff, counts = self.debug, -1, 0, {x: a.count(x) for x in a if a.count(x) == 2}

        if 2 not in counts.values():
            debug and print(f'Counts {counts}')
            return diff

        for key, value in counts.items():
            debug and print(f'{key} {value}')
            indices = [x for x, y in enumerate(a) if y == key]
            debug and print(indices)
            current_diff = indices[1] - indices[0]
            debug and print(f'current_diff {current_diff}')

            if element_diff == 0 or current_diff < element_diff:
                element_diff = current_diff

        return element_diff

    @staticmethod
    def _test_cases() -> list:
        """
        Format: dictionary item with 'kwargs' for inputs, 'result' for expected output
        :return: list
        """
        return [
            {'kwargs': {'a': [1, 2]}, 'result': -1},
            {'kwargs': {'a': [3, 2, 1, 2, 3]}, 'result': 2},
            {'kwargs': {'a': [7, 1, 3, 4, 1, 7]}, 'result': 3}
        ]
