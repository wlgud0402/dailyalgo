def longestWord(text):
    string_list = ""
    for string in text:
        try:
            if ("a" <= string <= "z") or ("A" <= string <= "Z"):
                string_list += string
            else:
                if string_list[-1] == " ":
                    continue
                else:
                    string_list += " "
        except:
            continue
    split_string_list = string_list.split()

    max_len = len(split_string_list[0])
    max_str = split_string_list[0]

    for string in split_string_list:
        if len(string) > max_len:
            max_str = string
            max_len = len(string)
    return max_str


print(longestWord(" ss "))

# string = "D"
# if string > "F":
#     print("big")
# else:
#     print("small")
