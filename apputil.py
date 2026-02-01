
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

if __name__ == "__main__":
    print(ways(12))
    print(ways(20))
    print(ways(3))
    print(ways(0))

import numpy as np

def lowest_score(names, scores):
    # Return the name of the student with the lowest test score.
    index = np.argmin(scores)
    # Return the name corresponding to the lowest score index
    return names[index]


def sort_names(names, scores):
    # Return the names sorted in descending order by their corresponding scores.
    sorted_indices = np.argsort(scores)[::-1]
    # Return names sorted by the sorted indices
    return names[sorted_indices]

if __name__ == "__main__":
    names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
    scores = np.array([99, 71, 85, 62, 91])
    print(lowest_score(names, scores))  # Should print 'Mauve'
    print(sort_names(names, scores))    # Should print names sorted by scores