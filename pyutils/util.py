import argparse


class Util:
    """
    Generic utility methods
    """

    @staticmethod
    def parse_args() -> tuple:
        """
        Boiler plate refactor for stock arg parsing for HR solutions
        :return: tuple
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--solution", type=str, help="the solution filename", required=True)
        parser.add_argument("--debug", type=int, help="enter debug Y/N", nargs='?', default=0, const=1)
        parser.add_argument("--show_help", type=int, help="enter for python def help Y/N", nargs='?', default=0, const=1)
        args = parser.parse_args()

        return args.solution.replace('-', '_'), bool(args.debug), args.show_help

    @staticmethod
    def format_output(result: bool, result_string: str) -> str:
        """
        Format output for success or failure results
        :param result: bool
        :param result_string: str
        :return: str
        """
        return Util.green_text(result_string) if result else Util.red_text(result_string)

    @staticmethod
    def red_text(my_string) -> str:
        """
        return string in red
        :param my_string: str
        :return:
        """
        return f'\033[1;31m{my_string}\033[0m'

    @staticmethod
    def green_text(my_string) -> str:
        """
        return string in green
        :param my_string: str
        :return:
        """
        return f'\033[1;32m{my_string}\033[0m'


if __name__ == '__main__':
    print('Not to be run directly')
