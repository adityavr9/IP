'''
    Monday, 9 October, 2017
'''
# We don't have macros on python
# Grade is not importrant, (7.5+) is decent
# Dijkstra's is helpful in non negative weighted graph's whereas BFS is helpful in non weighted graphs for shortest distance.
# Hash tables and collisions. --> Dictionaries, Linear Probing
# Dynamic Programming and Divide and Conquer use recursion
# Direct and Indirect recursion
# Direct: Function calling itself
# Indirect: f1 calling f2, f2 calling f1
# Base Case!
# Quadtry --> Indexing structure, Systems
# Many Funtional Programming languages use the paradigm of recursion.
# Recursion is not always helpful
# If we reduce our steps at every steps by 2, then our problem will be solved in logn2.
# During recursive call all the memory is used at once.
# Efficiency includes both time and space.


def powerEff(x, n, p=1):
    if n == 0:
        return p
    elif n == 1:
        return x * p
    elif n % 2 == 0:
        return powerEff(x ** 2, n // 2, p)
    else:
        return powerEff(x ** 2, n // 2, p * x)


def powerIneff(x, n):
    if x == 1:
        return 1
    else:
        return x * (x ** (n-1))
