def isValid(arr):
    if 1 in arr and 2 in arr:
        return False
    if 3 in arr and 4 in arr:
        return False
    if 5 in arr and 6 not in arr:
        return False
    if 6 in arr and 5 not in arr:
        return False
    if 7 not in arr and 8 not in arr:
        return False
    return True

print(isValid([1,3,7]))  # Output: True
print(isValid([7,1,2,3]))  # Output: False
print(isValid([1,5,6,7,3]))  # Output: True
