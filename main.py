# main.py
# Purpose: Provide a simple function that we can test with unittest.

def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


if __name__ == "__main__":
    # Simple manual check if you run it locally
    print(add(2, 3))  # expected 5
