import re

from dataclasses import dataclass
from importlib import import_module


@dataclass(slots=True)
class Solutions:

    solution_runner: str
    debug: bool = False
    show_help: bool = False
    package: str = "solutions_py"


    def import_solution(self) -> None:
        """
        Import the solution class and run
        :return: None
        """
        class_name = re.sub(r"[-_]", "", self.solution_runner.title())

        try:
            cls = getattr(import_module("." + self.solution_runner, package=self.package), class_name)(self.debug)
        except ModuleNotFoundError as exc:
            print(f"Module Not Found [ {self.solution_runner} ]. Check your spelling and try again.")
        else:
            if self.show_help:
                help(cls)
            else:
                cls.run()
        finally:
            self.debug and print("All done!")


if __name__ == "__main__":
    print("Go back to the root directory and run python solution_runner.py")
