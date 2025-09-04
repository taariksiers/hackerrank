import json

from rich import print
from rich.console import Console
from rich.table import Table


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
        if len(self._test_cases()) == 0:
            print(f"{self.__class__.__name__}: [red]No test cases present.[/red]")
            return

        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column(self.__class__.__name__, justify="right")
        table.add_column("Output")

        separate = len(self._test_cases()) > 1

        for test_case in self._test_cases():
            result = self.solution(**test_case['kwargs'])
            success = result == test_case['expected']
            output_color = "green" if success else "red"

            table.add_row("[b]Case Arguments[/b]", f"[yellow]{json.dumps(test_case['kwargs'], indent=4)}[/yellow]")
            table.add_row("[b]Expected[/b]", f"[purple]{test_case['expected']}[/purple]")
            table.add_row("[b]Result[/b]", f"[{output_color}]{result}[/{output_color}]")
            table.add_row("[b]Success[/b]", f"[b][{output_color}]{success}[/{output_color}][/b]")

            if separate:
                table.add_row("-------", "-------")


        console.print(table)

    def solution():
        """
        Implemented in lower level solution file
        """
        pass


if __name__ == '__main__':
    print('To be run from the root directory: `./solution_runner.py --solution athlete_sort --debug 1`')