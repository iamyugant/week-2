import numpy as np
# Given an amount n, return the number of ways to make change for n
def ways(n, coin_types=[1, 5]):
    # Initialize a list to store the number of ways to make change for each amount
    ways_list = [0] * (n + 1)
    # There is one way to make change for 0 amount: use no coins
    ways_list[0] = 1

    # Iterate through each coin type
    for coin in coin_types:
        # Update the ways_list for each amount from coin to n
        for amount in range(coin, n + 1):
            # Update the number of ways to make change for the current amount
            ways_list[amount] += ways_list[amount - coin]
    
    return ways_list[n]


print(ways(12))
print(ways(20))
print(ways(3))
print(ways(0))


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

