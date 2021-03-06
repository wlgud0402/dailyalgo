def addBorder(picture):
    width = len(picture[0]) + 2

    box = []
    for i in range(len(picture)+2):
        box.append("*" * width)

    for i in range(len(picture)):
        picture[i] = "*" + picture[i] + "*"

    for i in range(len(picture)):
        box[i+1] = picture[i]
    return box


print(addBorder(["abc", "ded"]))

# ["*****",
#  "*abc*",
#  "*ded*",
#  "*****"]
