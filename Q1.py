"""
Turn the snippet into a function.

"""



def compute_squares(nums: list[int]) -> list[int]:
    """
    Takes a list of integers and returns a list of their squares.
    """
    squares = []
    for n in nums:
        squares.append(n * n)
    return squares

# Testing the function
print(compute_squares([1, 2, 3, 4, 5]))
print(compute_squares([6, 7, 8]))
