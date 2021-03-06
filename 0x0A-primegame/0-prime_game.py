#!/usr/bin/python3
"""game of primes"""


def prime_or_not(n):
    """checks n is prime or not
    """
    if n == 1:
        return False
    if n == 2:
        return True
    d = n // 2 + 1
    while d > 1:
        if n % d == 0:
            return False
        d = d - 1
    return True


def winner(x, nums):
    """returns the round winner
    """
    count = 0
    try:
        if x < 1 and len(nums) < 0:
            return None
        for p in range(x):
            if prime_or_not(nums[p]):
                count += 1
    except Exception:
        return None
    if count % 2 == 0 or x == 1:
        return "Ben"
    return "Maria"


def isWinner(x, nums):
    """plays game of primes and returns the winner
    """
    Ben = 0
    Maria = 0
    game = None
    if x <= 10000 and len(nums) <= 10000:
        for r in range(x):
            numlist = []
            for num in range(nums[r] + 1):
                numlist.append(num + 1)
            game = winner(nums[r], numlist)
            if game == "Ben":
                Ben += 1
            if game == "Maria":
                Maria += 1
        if Ben > Maria:
            return "Ben"
        if Maria > Ben:
            return "Maria"
        return None
