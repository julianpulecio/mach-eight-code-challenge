"""
finds pairs of integers from a list thatsum to a given value.

Parameters:
    numbers (list): List of integers.
    target (int): Target sum.

Returns:
    pairs (list): List of frozensets, each containing a pair of integers that sum to the target.

"""
def find_pairs(numbers:list, taget:int) ->list:
    result = []
    
    for number_one in numbers:
        for number_two in numbers:
            if number_one + number_two == target:
                result.append({number_one,number_two})
    
    return list(set(frozenset(item) for item in result))