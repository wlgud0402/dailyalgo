# def fileNaming(names):
#     answer = []
#     count = {}
#     for name in names:
#         if name in count:
#             count[name] += 1
#             new = name+"("+str(count[name])+")"
#             if new in count:
#                 while new in count:
#                     count[name] += 1
#                     new = name+"("+str(count[name])+")"
#                 answer.append(new)
#                 count[new] = 0
#                 continue
#             answer.append(new)
#             count[new] = 0
#         else:
#             answer.append(name)
#             count[name] = 0
#     return answer

def fileNaming(names):
    for i in range(len(names)):
        if names[i] in names[:i]:
            j = 1
            while names[i]+"("+str(j)+")" in names[:i]:
                j += 1
            names[i] += "("+str(j)+")"
    return names


print(fileNaming(["doc", "doc", "image", "doc(1)", "doc"]))
# ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"]
