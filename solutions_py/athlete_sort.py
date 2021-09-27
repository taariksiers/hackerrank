from solutions_py.harness import Harness


class AthleteSort(Harness):
    """
    https://www.hackerrank.com/challenges/python-sort-sort/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
    You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and
    so on). You are required to sort the data based on the Kth attribute and print the final resulting table.
    """

    def solution(self, arr: list) -> list:
        sort_by = int(arr.pop(-1))
        n, m = [int(arg) for arg in arr.pop(0).split(" ")]

        cleaned = list()
        for item in arr:
            item_casted = [int(x) for x in item.split(" ")]
            cleaned.append(item_casted)

        outputs = sorted(cleaned, key=lambda x: x[sort_by])
        result = list()

        for clean in outputs:
            result.append(" ".join([str(y) for y in clean]))

        return result

    @staticmethod
    def _test_cases() -> list:
        """
        Format: dictionary item with 'kwargs' for inputs, 'result' for expected output
        :return: list
        """
        return [
            {"kwargs": {"arr": ["5 3", "10 2 5", "7 1 0", "9 9 9", "1 23 12", "6 5 9", "1"]},
             "result": ["7 1 0", "10 2 5", "6 5 9", "9 9 9", "1 23 12"]}
        ]
