def is_between_and_even(test_value, low_value, high_value):
    if low_value <= test_value <= high_value:
        if not test_value % 2:
            return True
        else:
            return False
    else:
        return False


print(is_between_and_even(23, 22, 24))
print(is_between_and_even(22.0, 22.0, 24.5))
print(is_between_and_even(21.99, 22.0, 24.5))
