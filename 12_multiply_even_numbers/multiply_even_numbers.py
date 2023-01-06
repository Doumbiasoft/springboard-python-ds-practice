def multiply_even_numbers(nums):
    """Multiply the even numbers.

        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48

        >>> multiply_even_numbers([3, 4, 5])
        4

    If there are no even numbers, return 1.

        >>> multiply_even_numbers([1, 3, 5])
        1
    """

    sum_even_numbers = 1

    for number in nums:
        if number % 2 == 0:
            sum_even_numbers *= number
    return sum_even_numbers
