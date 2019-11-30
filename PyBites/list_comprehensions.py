def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""

    new_list = [x for x in numbers if x % 2 == 0]
    return_list = [x for x in new_list if x > 0]
    return return_list