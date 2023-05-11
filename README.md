# NAME

Function::find_pairs

# Description

 This function finds pairs of integers from a list thatsum to a given value.


# plain function
```python
pairs = find_pairs(numbers, target)
```
# Arguments
- numbers (list): A list of integers.
- target (int): The target value that pairs of numbers should add up to.

# Return Value
 - pairs (list): List of frozensets, each containing a pair of integers that sum to the target.


# Example
```python
numbers = [1, 9, 5, 0, 20, -4, 12, 16, 7]
target = 12
pairs = find_pairs(numbers, target)
print(pairs)
```
This will output
```python
[frozenset({16, -4}), frozenset({0, 12}), frozenset({5, 7})]
```