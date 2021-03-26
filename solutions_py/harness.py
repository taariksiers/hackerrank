from pyutils import Util


class Harness:
    """
    Created to re-use init and run the main solution runner
    """
    def __init__(self, debug=False) -> None:
        """
        :param debug: bool
        """
        self.debug = debug

    def run(self) -> None:
        """
        Run through each test case, compare results and print success/fail
        :return: None
        """
        for test_case in self._test_cases():
            print(f"Case Arguments: {test_case['kwargs']}")
            result = self.solution(**test_case['kwargs'])
            success = result == test_case['result']
            print(f"Expected {Util.green_text(test_case['result'])} | Result {Util.format_output(success, result)}")
            print(f"Success: {Util.format_output(result, success)}\n------------------")
