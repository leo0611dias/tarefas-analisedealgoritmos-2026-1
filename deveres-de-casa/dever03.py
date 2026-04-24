def is_palindrome(array):
    """
    Checks if an array is a palindrome using recursion.
    """
    # empty array or array with one element
    if len(array) == 0 or len(array) == 1:
        return True

    elif array[0] != array[-1]:
        return False

    else:
        return is_palindrome(array[1:-1])


array1 = [0, 1, 2, 3, 2, 1, 0]
print(is_palindrome(array1))

array2 = ["a", "b", "b", "a"]
print(is_palindrome(array2))

array3 = ["a", "b", "c", "b", "a"]
print(is_palindrome(array3))

array4 = ["a", "b", "c", "f", "b", "a"]
print(is_palindrome(array4))
