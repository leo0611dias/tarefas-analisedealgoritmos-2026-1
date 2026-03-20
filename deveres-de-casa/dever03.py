def eh_palindromo(arr, inicio=0, fim=None):
    if fim is None:
        fim = len(arr) - 1
      
    if inicio >= fim:
        return True

    # se os extremos forem diferentes, não é palíndromo
    if arr[inicio] != arr[fim]:
        return False

    # chamada recursiva indo para o centro
    return eh_palindromo(arr, inicio + 1, fim - 1)

array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]

print(eh_palindromo(array1))  # True
print(eh_palindromo(array2))  # True
print(eh_palindromo(array3))  # True
print(eh_palindromo(array4))  # False
