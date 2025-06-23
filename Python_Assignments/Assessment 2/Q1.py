"""
Turn the snippet into a function.

"""



def compute_squares(nums: list[int]) -> list[int]:

    squares = []
    for n in nums:
        squares.append(n * n)
    return squares

print(compute_squares([1, 2, 4, 10]))
print(compute_squares([6, 7, 8]))
