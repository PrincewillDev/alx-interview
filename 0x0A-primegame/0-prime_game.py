#!/usr/bin/python3
"""This module contains functions that finds the winner of a prime
number game problem

functions   - sieveOfEratosthenes
            - isWinner
"""


def sieveOfEratosthenes(n):
    """This function finds the number of prime numbers in a given range

    Args:
        n (int): given number to find the prime numbers within

    Returns:
        int: number of prime numbers  in the given range
    """

    prime = [True for i in range(n + 1)]
    p = 2
    count = 0

    while (p * p <= n):
        if(prime[p] is True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, n + 1):
        if prime[p]:
            count += 1
    return count


def isWinner(x, nums):
    """This function finds the winner of a prime number game problem
    after a number of rounds

    Args:
        x (int): number of rounds to be played in the game
        nums (int): number range of which players will pick prime numbers from
    """

    ben = 0
    maria = 0

    for i in range(x):
        primeCount = sieveOfEratosthenes(nums[i])
        if primeCount % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return("Ben")
    elif maria > ben:
        return("Maria")
    else:
        return None
