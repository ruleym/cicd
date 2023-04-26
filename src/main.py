"""
Perfect square checker
Author: Molly Ruley
"""


def is_square(num: int) -> bool:
    """Return True if num is a perfect square, False otherwise."""
    if num == 0:
        return False
    else:
        return (num ** .5).is_integer()


def is_square_str(num: str) -> str:
    """Return a string indicating whether num is a perfect square or not."""
    if num.isnumeric():
        return f"{num} is {'a perfect square' if is_square(int(num)) else 'not a perfect square'}."
    else:
        return "Please enter a number."

