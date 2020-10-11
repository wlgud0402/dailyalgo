def reverseInParentheses(inputString):
    inputString = list(inputString)
    while True:
        left_idx = 0
        right_idx = 0
        for idx, s in enumerate(inputString):
            if s == "(":
                left_idx = idx

            if s == ")":
                right_idx = idx

                reverse_part = inputString[left_idx+1:right_idx][::-1]
                inputString[left_idx:right_idx+1] = reverse_part
                break
        if "(" not in inputString:
            return "".join(inputString)

    # inputString = list(inputString)
    # reverse_part = inputString[8:11][::-1]
    # inputString[7:11+1] = reverse_part
    # print(inputString)
    # print(reverse_part)


print(reverseInParentheses("foo(bar(baz))blim"))
# "foo(bar(baz))blim" => "foo(barzab)blim" => "foobazrabblim".
