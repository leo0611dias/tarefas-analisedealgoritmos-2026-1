import time
import sys

# Adjusted recursion limit
sys.setrecursionlimit(1500)


def factorial(number):
    """
    Calculates the factorial of the given number.
    """
    # Factorial is not designed for calculating negative numbers
    if number < 0:
        print("It must be a non-negative number!")
        return None

    # The factorial of 0 and 1 is always 1
    elif number == 0 or number == 1:
        return 1

    # Positive number greater than 1
    else:
        # Recursive step: multiply number by factorial of (number - 1)
        return number * factorial(number - 1)


def run_factorial_benchmark(number):
    """
    Runs the performance test for each scale defined.
    """
    start_factorial = time.perf_counter()
    result = factorial(number)
    end_factorial = time.perf_counter()

    time_factorial = end_factorial - start_factorial

    # Output
    print(f"\nFactorial Result of {number}: {result}")
    print(f"{number} - Execution time: {time_factorial:.6f}s")


if __name__ == "__main__":
    # User's input
    number = int(input("Insert the number to be calculated: "))
    run_factorial_benchmark(number)

    test_values = [10, 100, 500, 1000]
    for i in test_values:
        run_factorial_benchmark(i)
