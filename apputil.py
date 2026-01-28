import numpy as np

def ways(n, coin_types=[1, 5]):
    ways_list = [0] * (n + 1)
    ways_list[0] = 1

    for coin in coin_types:
        for amount in range(coin, n + 1):
            ways_list[amount] += ways_list[amount - coin]

    return ways_list[n]

print(ways(12))
print(ways(20))
print(ways(3))
print(ways(0))