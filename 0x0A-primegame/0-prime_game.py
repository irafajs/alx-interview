#!/usr/bin/python3
"""
Shebang to create a PY script
"""


def consecutive_num(n):
    """method to generate consecutive number"""
    cons_list = []
    for i in range(n + 1):
        if i == 0:
            continue
        cons_list.append(i)
    return cons_list


def pop_multiple(cons_list, chosen_number):
    """method to pop the choosen number from the list"""
    multiples = [i for i in cons_list if i % chosen_number == 0]
    for multiple in multiples:
        cons_list.remove(multiple)
    return cons_list


def is_prime(num):
    """method to cehck if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """method to check the game winner"""
    if x == 0 or x is None or len(nums) == 0:
        return None
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        cons_list = consecutive_num(n)

        maria_turn = True
        while cons_list:
            prime_numbers = [i for i in cons_list if is_prime(i)]
            if not prime_numbers:
                break
            if maria_turn:
                prime_choice = min(prime_numbers)
                cons_list = pop_multiple(cons_list, prime_choice)
            else:
                prime_choice = min(prime_numbers)
                cons_list = pop_multiple(cons_list, prime_choice)
            maria_turn = not maria_turn

        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
