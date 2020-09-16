def solution(string, n):
    string = list(string)
    big = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    small=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for i in range(len(string)):
        if string[i] == ' ':
            continue

        before = string[i]
        if before in big:
            idx = (big.index(before)+n) % 26
            string[i] = big[idx]
        else:
            idx = (small.index(before)+n) % 26
            string[i] = small[idx]
    return ''.join(string)


print(solution("a B z",4))
