from solutions_py.harness import Harness


class IceCreamParlor(Harness):
    """
    https://www.hackerrank.com/challenges/icecream-parlor/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
    Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.
    Return an array containing the indices of the prices of the two flavors they buy, sorted ascending.
    """
    def solution(self, m, arr, start=0) -> list:
        """
        Parameters
        ----------
        m : int
            total budget to spend
        arr : list
            cost of each flavour

        Returns
        -------
        list
            A list of indices of the prices of the two flavors they buy, sorted ascending.
        :param m: int
        :param arr: list
        :param start: int
        :return: list
        """
        debug, flavour_sum, flavours = self.debug, 0, []

        for flavour, cost_price in enumerate(arr, start=1):
            debug and print(f'Flavour Index: {flavour} | Cost {cost_price} | Flavour Sum {flavour_sum}')

            if cost_price >= m:
                debug and print(f'Skipping...')
                continue

            if flavour == 1:
                flavour_sum = cost_price
                flavours.append(flavour + start)
                debug and print(f'Adding first {flavour} at cost {cost_price} | flavour sum {flavour_sum}')
                continue

            if (flavour_sum + cost_price) == m and (len(flavours) == 1):
                debug and print(f'Adding next {flavour} at cost {cost_price}')
                flavours.append(flavour + start)
                break

        if len(flavours) != 2 and len(arr) > 1:
            debug and print(f'No available combos for this run, popping and recalling...')
            arr.pop(0)
            start += 1
            flavours = self.solution(m, arr, start)

        debug and print(flavours)

        return flavours

    @staticmethod
    def _test_cases() -> list:
        """
        Format: dictionary item with 'kwargs' for inputs, 'result' for expected output
        :return: list
        """
        return [
            {'kwargs': {'m': 4, 'arr': [1, 4, 5, 3, 2]}, 'result': [1, 4]},
            {'kwargs': {'m': 4, 'arr': [2, 2, 4, 3]}, 'result': [1, 2]},
            {'kwargs': {'m': 9, 'arr': [1, 3, 4, 6, 7, 9]}, 'result': [2, 4]},
            {'kwargs': {'m': 8, 'arr': [1, 3, 4, 4, 6, 8]}, 'result': [3, 4]},
            {'kwargs': {'m': 3, 'arr': [1, 2]}, 'result': [1, 2]}
        ]
