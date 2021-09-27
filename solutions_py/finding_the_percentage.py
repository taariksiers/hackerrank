from solutions_py.harness import Harness


class FindingThePercentage(Harness):
    """
    https://www.hackerrank.com/challenges/finding-the-percentage/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
    The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
    Print the average of the marks array for the student name provided, showing 2 places after the decimal.
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
