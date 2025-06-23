"""
Write a function that reads a text file and returns its
lines.

"""



def read_lines(filename: str) -> list[str]:
    """
    Reads all lines from the given file and returns them as a list of strings.
    """
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def compute_squares(nums: list[int]) -> list[int]:
    """
    Returns a list of squares for the given list of integers.
    """
    return [n * n for n in nums]

def main():
    filename = input("Enter filename to read: ")
    lines = read_lines(filename)
    print(f"Line count: {len(lines)}")

    # Example usage of compute_squares
    print(compute_squares([1, 2, 3]))
    print(compute_squares([4, 5, 6]))

if __name__ == "__main__":
    main()
