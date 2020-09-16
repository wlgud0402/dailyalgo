def solution(string):
    string = string.upper()
    count_P=0
    count_Y=0
    for alphabet in string:
        if alphabet == "P":
            count_P+=1
        elif alphabet == "Y":
            count_Y+=1
    if count_P == 0 and count_Y ==0:
        return True
    elif count_P == count_Y:
        return True
    else:
        return False

print(solution("pppyy"))

def numPY(s):
    return s.lower().count('p') == s.lower().count('y')


print( numPY("pPoooyY") )
print( numPY("Pyy") )

