import re

from solutions_py.harness import Harness


class ValidatingCreditCardNumbers(Harness):
    """
    https://www.hackerrank.com/challenges/validating-credit-card-number/problem
    You and Fredrick are good friends. Yesterday, Fredrick received credit cards from ABCD Bank. He wants to verify
    whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
    A valid credit card from ABCD Bank has the following characteristics:
    """

    max_sequence = 4

    def solution(self, arr: list) -> list:
        debug, valid = self.debug, True
        cc_cleaned = str(arr).strip()
        invalid_chars = re.search('[ |_]{1,}', cc_cleaned)

        if invalid_chars is not None:
            debug and print("False: space or underscore found")
            valid = False

        dash_split = cc_cleaned.split('-')

        len_counts = 0
        if len(dash_split) > 1:
            len_counts = [len(x) for x in dash_split if len(x) > 4]

        current = {"num": None, "count": 0}
        digits = re.search(r"\d+", cc_cleaned.replace('-', ''))

        for num in digits[0]:
            if current["num"] is None or current["num"] != num:
                current["num"] = num
                current["count"] = 1
            else:
                current["count"] += 1

            if current["count"] >= 4:
                valid = False
                debug and print("False: has series of the same number")

        if int(cc_cleaned[0]) not in [4,5,6]:
            debug and print("False: Does not start with 4,5,6")
            valid = False

        if len(cc_cleaned.replace('-', '').strip()) != 16:
            debug and print("False: Does not have 16 digits")
            valid = False

        if digits is None or len(digits[0]) != 16:
            debug and print("False: Does not have any digits or has alphas")
            valid = False

        if len_counts and len_counts[0] > 4:
            debug and print("False: has subset greater > 4")
            valid = False

        debug and print(f"cc_cleaned {cc_cleaned} | {cc_cleaned[0]} | {digits[0]} | {dash_split} | {len_counts} | V {valid}")

        return "Valid" if valid else "Invalid"

    @staticmethod
    def _test_cases() -> list:
        """
        Format: dictionary item with 'kwargs' for inputs, 'result' for expected output
        :return: list
        """
        return [
            {"kwargs": {"arr": "4123456789123456"}, "result": "Valid"},
            {"kwargs": {"arr": "5123-4567-8912-3456"}, "result": "Valid"},
            {"kwargs": {"arr": "61234-567-8912-3456"}, "result": "Invalid"},
            {"kwargs": {"arr": "4123356789123456"}, "result": "Valid"},
            {"kwargs": {"arr": "5133-3367-8912-3456"}, "result": "Invalid"},
            {"kwargs": {"arr": "5123 - 3567 - 8912 - 3456"}, "result": "Invalid"},
            {"kwargs": {"arr": "7165863385679329"}, "result": "Invalid"},
            {"kwargs": {"arr": "6175824393389297"}, "result": "Valid"},
            {"kwargs": {"arr": "5252248277877418"}, "result": "Valid"},
            {"kwargs": {"arr": "9563584181869815"}, "result": "Invalid"},
            {"kwargs": {"arr": "5179123424576876"}, "result": "Valid"},
            {"kwargs": {"arr": "3695-7963-  5827-75"}, "result": "Invalid"},
            {"kwargs": {"arr": "4143-4672-8798-2968-2968"}, "result": "Invalid"},
            {"kwargs": {"arr": "6865---------------3965---------------1564-------------2918"}, "result": "Invalid"},
            {"kwargs": {"arr": "6865396515642918"}, "result": "Valid"},
        ]
