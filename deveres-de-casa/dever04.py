import math


def F(n):
    """
    Function that calculates the value of F(n) using recursion
    """
    if n == 1:  # base case
        return 2

    return 2 * F(n - 1) + n**2  # recursive call


def closed_formula(n):
    """
    Function that calculates the value of F(n) using the closed formula
    """
    # F(n) = 2^n * F(1) + sum of k^2 * 2^(n-k) for k=2 till n
    resultado = 2**n * 2  # homogeneous part: 2^n * F(1)

    for k in range(2, n + 1):
        resultado += (k**2) * (2 ** (n - k))

    return resultado


if __name__ == "__main__":

    n = int(input("Type the value of n: "))

    if n < 1:
        print("n must be greater than or equal 1.")
    else:
        recursive_result = F(n)
        closed_result = closed_formula(n)

        print(f"\nF({n}) by recursion = {recursive_result}")
        print(f"F({n}) by closed formula = {closed_result}") 
