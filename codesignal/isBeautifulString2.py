import string


def isBeautifulString(inputString):
    before = 50
    for alpha in string.ascii_lowercase:
        count = inputString.count(alpha)
        if count > before:
            return False
        before = count

    return True


print(isBeautifulString("aaabb"))  # true
