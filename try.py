def safe_divide(a, b):
    """Divide a by b, handling common errors with try/except."""
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"{a} / {b} -> Error: cannot divide by zero")
        return None
    except TypeError:
        print(f"{a!r} / {b!r} -> Error: both values must be numbers")
        return None
    else:
        print(f"{a} / {b} -> {result}")
        return result
    finally:
        print("  (division attempt finished)")


def to_int(text):
    """Convert text to an int, returning None if it isn't a valid number."""
    try:
        return int(text)
    except ValueError:
        print(f"'{text}' is not a valid number")
        return None


if __name__ == "__main__":
    safe_divide(10, 2)
    safe_divide(5, 0)
    safe_divide("10", 2)

    print()
    for text in ["42", "abc", "-7"]:
        number = to_int(text)
        if number is not None:
            print(f"'{text}' -> {number}")
