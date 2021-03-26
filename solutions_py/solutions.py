from importlib import import_module
import re


class Solutions:

    def __init__(self, solution_runner, debug=False, show_help=False):
        """
        Initialise with solution to run
        :param solution_runner: str
        :param debug: bool
        :param show_help: bool
        """
        self.solution_runner = solution_runner
        self.debug = debug
        self.show_help = show_help
        self.package = 'solutions_py'

        self._import_solution()

    def _import_solution(self) -> None:
        """
        Import the solution class and run
        :return: None
        """
        class_name = re.sub(r'[-_]', '', self.solution_runner.title())

        try:
            cls = getattr(import_module('.' + self.solution_runner, package=self.package), class_name)(self.debug)
        except ModuleNotFoundError as exc:
            print(f'Module Not Found [ {self.solution_runner} ]. Check your spelling and try again.')
        else:
            if self.show_help:
                help(cls)
            else:
                cls.run()
        finally:
            self.debug and print('All done!')

    def __str__(self):
        pass


if __name__ == '__main__':
    print('Go back to the root directory and run python solution_runner.py')
