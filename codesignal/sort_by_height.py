def sortByHeight(array):
    tree = []
    for i, v in enumerate(array):
        if array[i] == -1:
            tree.append(i)
    
    array.sort()
    for i in range(len(tree)):
        array.pop(0)
    
    for idx in tree:
        array.insert(idx, -1)

    return array






print(sortByHeight([23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]))