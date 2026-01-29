"""Utility functions for Exercise 1."""

def ways(cents, coin_types=[1, 5]):
    """Return the number of ways to make cents using given coin values.

    Coin order does not matter.

    Args:
        cents: A non-negative integer representing cents.
        coin_types: A list of coin values. Defaults to [1, 5].

    Returns:
        The number of ways to make cents.
    """
    ways_list = [0] * (cents + 1)
    ways_list[0] = 1

    for coin in coin_types:
        for amount in range(coin, cents + 1):
            ways_list[amount] += ways_list[amount - coin]

    return ways_list[cents]


"""Utility functions for Exercise 2."""

import numpy as np


def lowest_score(names, scores):
    """Return the name of the student with the lowest score.

    Args:
        names: A NumPy array of student names.
        scores: A NumPy array of student scores.

    Returns:
        The name of the student with the lowest score.
    """
    index = np.argmin(scores)
    return names[index]


def sort_names(names, scores):
    """Return student names sorted by descending test score.

    Args:
        names: A NumPy array of student names.
        scores: A NumPy array of student scores.

    Returns:
        A NumPy array of names sorted from highest to lowest score.
    """
    sorted_indices = np.argsort(scores)[::-1]
    return names[sorted_indices]
