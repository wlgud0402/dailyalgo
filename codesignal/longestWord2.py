def longestWord(text):
    string_list = ""
    for string in text:
        if ("a" <= string <= "z") or ("A" <= string <= "Z"):
            string_list += string
        else:
            if string_list[-1] == " ":
                continue
            else:
                string_list += " "
    split_string_list = string_list.split()

    max_len = len(split_string_list[0])
    max_str = split_string_list[0]

    for string in split_string_list:
        if len(string) > max_len:
            max_str = string
            max_len = len(string)
    return max_str


print(longestWord("You are the best!!!!!!!!!!![[!]] CodeFighter ever!"))

# string = "D"
# if string > "F":
#     print("big")
# else:
#     print("small")
