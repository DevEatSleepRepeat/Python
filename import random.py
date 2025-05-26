import random
def cool_function(n):
    """
    A cool function that generates n random numbers between 1 and 100, then returns the sum of those numbers.

    Parameters:
    n (int): The number of random numbers to generate.

    Returns:
    int: The sum of n randomly generated numbers between 1 and 100.
    """
    total = 0
    for i in range(n):
        random_number = random.randint(1, 100)
        total += random_number
    return total
print(cool_function(12))
