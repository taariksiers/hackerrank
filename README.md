# Hackerrank exercises

Bookmark repo for all [Hackerrank](https://www.hackerrank.com/) exercises attempted.

Solutions initially done in PHP but now Python going forward.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![PHP](https://img.shields.io/badge/php-%23777BB4.svg?style=for-the-badge&logo=php&logoColor=white)![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

<!-- https://github.com/Ileriayo/markdown-badges -->


## Exercises:
- [Beautiful Binary String](solutions_php/beautiful-binary-string.php)
- [Counting Valleys](solutions_php/counting-valleys.php)
- [Drawing Book](solutions_php/drawing-book.php)
- [Electronics Shop](solutions_php/electronics-shop.php)
- [Find The Median](solutions_php/find-the-median.php)
- [Game of Thrones](solutions_php/game-of-thrones.php)
- [Hackerrank in a string](solutions_php/hackerrank-in-a-string.php)
- [Halloween Party](solutions_php/halloween-party.php)
- [Ice-cream Parlor](solutions_py/ice_cream_parlor.py)
- [Jumping on the clouds](solutions_php/jumping-on-the-clouds.php)
- [Lonely Integer](solutions_php/lonely-integer.php)
- [Making anagrams](solutions_php/making-anagrams.php)
- [Minimum Distances](solutions_py/minimum_distances.py)
- [Missing numbers](solutions_py/missing_numbers.py)
- [Palindrome Index](solutions_php/palindrome-index.php)
- [Repeated String](solutions_php/repeated-string.php)
- [Running time](solutions_php/runningtime.php)
- [Sherlock and the valid string](solutions_php/sherlock-and-valid-string.php)
- [Sock Merchant](solutions_php/sock-merchant.php)
- [String Construction](solutions_php/string-construction.php)
- [Utopian tree](solutions_php/utopian-tree.php)

## Python Challenges:
- [List Comprehensions](solutions_py/list_comprehensions.py)

## Algorithms Sorting
- [Insertion Sort 1](interview_practice/insertionsort1.py) | ([PHP version](solutions_php/insertionsort1.php))
- [Insertion Sort 2](interview_practice/insertionsort2.py) | ([PHP version](solutions_php/insertionsort2.php))
- [Quick sort](interview_practice/quicksort1.py)
- [Counting Sort](interview_practice/countingsort1.py)

---

## Python requirements.txt

```bash
pyenv shell [your preferred version here]
python3 -m venv venv
python3 -m pip install -r requirements-to-freeze.txt --upgrade
python3 -m pip freeze > requirements.txt

cd solutions_py
PYTHONPATH=$PYTHONPATH:$(pwd)
```

## Running Python solutions

**Filename example**: `solutions_py/ice_cream_parlor.py`

```bash
./solution_runner.py --solution=ice_cream_parlor
```
<details>
    <Summary>Sample output</Summary>

```bash
Case Arguments: {'m': 4, 'arr': [1, 4, 5, 3, 2]}
Expected [1, 4] | Result [1, 4]
Success: True
------------------
Case Arguments: {'m': 4, 'arr': [2, 2, 4, 3]}
Expected [1, 2] | Result [1, 2]
Success: True
------------------
Case Arguments: {'m': 9, 'arr': [1, 3, 4, 6, 7, 9]}
Expected [2, 4] | Result [2, 4]
Success: True
------------------
Case Arguments: {'m': 8, 'arr': [1, 3, 4, 4, 6, 8]}
Expected [3, 4] | Result [3, 4]
Success: True
------------------
Case Arguments: {'m': 3, 'arr': [1, 2]}
Expected [1, 2] | Result [1, 2]
Success: True
```
</details></details>


### Optional arguments

Debug:

```bash
./solution_runner.py --solution=ice_cream_parlor --debug=1
```

Help
```bash
./solution_runner.py --solution=ice_cream_parlor --show_help
```

<details>
    <summary>Sample output</summary>

```bash
Help on IceCreamParlor in module solutions_py.ice_cream_parlor object:

class IceCreamParlor(solutions_py.harness.Harness)
 |  IceCreamParlor(debug=False) -> None
 |
 |  https://www.hackerrank.com/challenges/icecream-parlor/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
 |  Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.
 |  Return an array containing the indices of the prices of the two flavors they buy, sorted ascending.
 |
 |  Method resolution order:
 |      IceCreamParlor
 |      solutions_py.harness.Harness
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  solution(self, m, arr, start=0) -> list
 |      Parameters
 |      ----------
 |      m : int
 |          total budget to spend
 |      arr : list
 |          cost of each flavour
 |
 |      Returns
 |      -------
 |      list
 |          A list of indices of the prices of the two flavors they buy, sorted ascending.
 |      :param m: int
 |      :param arr: list
 |      :param start: int
 |      :return: list
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from solutions_py.harness.Harness:
 |
 |  __init__(self, debug=False) -> None
 |      :param debug: bool
 |
 |  run(self) -> None
 |      Run through each test case, compare results and print success/fail
 |      :return: None
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from solutions_py.harness.Harness:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 (END)
 ```
</details>
