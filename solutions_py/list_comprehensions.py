from solutions_py.harness import Harness


class ListComprehensions(Harness):

    def solution(self, arr) -> list:
        """
        Create permutations from given array then use list comp to exclude == sum_max
        Update multi nested loop to generator to avoid OOM errors
        :param arr: list
        :return: list
        """
        [x, y, z, sum_max] = arr[:4]
        self.debug and print(f"{x}, {y}, {z}, {sum_max}")

        permutations: list = []

        for x_coord in range(x+1):
            for y_coord in range(y+1):
                for z_coord in range(z+1):
                    permutations.append([x_coord, y_coord, z_coord])

        return [permutation for permutation in permutations if sum(permutation) != sum_max]

    @staticmethod
    def _test_cases() -> list:
        """
        Format: dictionary item with 'kwargs' for inputs
        :return: list
        """
        return [
            {"kwargs": {"arr": [1, 1, 2, 3]}, "expected": [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]},
            {"kwargs": {"arr": [1, 1, 1, 2]}, "expected": [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]},
            {"kwargs": {"arr": [1, 1, 2, 2]}, "expected": [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2]]},
            {"kwargs": {"arr": [2, 2, 2, 2]}, "expected": [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]},
        ]
