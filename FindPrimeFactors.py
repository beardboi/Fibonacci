#  Copyright 2020 Diego Bravo B, diego.bravo@alumnos.ucn.cl
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software
#  and associated documentation files (the "Software"), to deal in the Software without
#  restriction, including without limitation the rights to use, copy, modify, merge, publish,
#  distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom
#  the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or
#  substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
#  BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import math


# The function return the fibonacci number.
def fibonacci(number):
    if number < 2:
        return number
    else:
        result = fibonacci(number - 2) + fibonacci(number - 1)
        return result


# This functions find all the prime factors given certain number.
def factorization(number):
    # Count for the times that a factor appears
    count = 0

    # While the number is divisible by 2
    while number % 2 == 0:
        number = number / 2
        count += 1

    # Print the factor
    if count > 1:
        print(f'{2}^{count} x', end=' ')

    # Check all the possible numbers that are factors
    for i in range(3, int(math.sqrt(number) + 1), 2):
        # Count for the times that a factor appears
        count = 0

        while number % i == 0:
            count += 1
            number = int(number / i)

        # If the numbers is a factor print it
        if count == 1:
            print(f'{i} x', end=' ')
        elif count > 1:
            print(f'{i}^{count} x', end=' ')

    # If the last one is a prime number
    if number > 2:
        print(f'{number}', end=" ")

    print('')


# The main program.
def main():
    print('App started it, computing the fibonacci sequence...')
    print(' ')

    # Loop trough all the fib numbers.
    for i in range(300):
        # Calculate and save the fib number.
        fibNumber = fibonacci(i + 1)

        print(f'{i + 1} - {fibNumber} =', end=' ')
        factorization(fibNumber)

    print('Done.')


def test():
    factorization(14930352)


# The entry point of the app.
if __name__ == '__main__':
    main()
