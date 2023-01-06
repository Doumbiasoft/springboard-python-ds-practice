def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    
    occurences = {}

    for num in nums:
        occurences[num] = occurences.get(num, 0) + 1

    for (key_number, value_number) in occurences.items():
        if value_number == max(occurences.values()):
            return key_number

