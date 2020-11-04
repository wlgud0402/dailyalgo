def circleOfNumbers(n, firstNumber):
    if (n // 2) + firstNumber >= n:
        return ((n//2) + firstNumber) % n
    else:
        return (n // 2) + firstNumber
