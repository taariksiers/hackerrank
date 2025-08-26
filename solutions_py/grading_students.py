from solutions_py.harness import Harness


class GradingStudents(Harness):
    """
    https://www.hackerrank.com/challenges/grading/problem
    Given the initial value of n for each of Sam's students, write code to automate the rounding process.
    """

    ROUND_NOT = 38
    ROUND_DIFF = 3
    MULTIPLE = 5

    def solution(self, arr: list) -> list:

        rounded = []

        for grade in arr:
            if grade < self.ROUND_NOT:
                rounded.append(grade)
                continue

            rounded.append(self._check_up_round(grade))

        return rounded

    def _check_up_round(self, grade: int) -> int:
        diff = 1
        for next_score in range(grade+1, grade + self.MULTIPLE):
            if next_score % self.MULTIPLE == 0 and diff < self.ROUND_DIFF:
                return next_score
            diff += 1
        return grade

    @staticmethod
    def _test_cases() -> list:
        """
        Format: dictionary item with 'kwargs' for inputs, 'result' for expected output
        :return: list
        """
        return [
            {
                "kwargs": {"arr": [73, 67, 38, 33]},
                "expected": [75, 67, 40, 33]
                }
                ]
