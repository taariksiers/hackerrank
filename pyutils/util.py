import argparse


class Util:
    """
    Generic utility methods
    """

    @staticmethod
    def parse_args() -> tuple:
        """
        Boilerplate refactor for stock arg parsing for HR solutions
        :return: tuple
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--solution", type=str, help="the solution filename", required=True)
        parser.add_argument("--debug", type=int, help="enter debug Y/N", nargs='?', default=0, const=1)
        parser.add_argument("--show_help", type=int, help="enter for python def help Y/N", nargs='?', default=0, const=1)
        args = parser.parse_args()

        return args.solution.replace('-', '_'), bool(args.debug), args.show_help


if __name__ == '__main__':
    print('Not to be run directly')
