def makeArrayConsecutive2(statues):
    statues.sort()

    compare = [i for i in range(statues[0],statues[-1]+1)]
    return len(compare) - len(statues)


print(makeArrayConsecutive2([6,2,3,8]))