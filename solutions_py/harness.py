from pyutils import Util
from rich import print


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
            success = result == test_case['expected']
            print(f"Expected: [purple]{test_case['expected']}[/purple]")

            output_color = "green" if success else "red"
            print(f"Result: [{output_color}]{result}[/{output_color}]")
            print(f"Success: [{output_color}]{success}[/{output_color}]")

            print("\n------------------")
