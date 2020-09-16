paths = [["B","C"],["D","B"],["C","A"]]
pathss = [["B","C"],["D","B"],["C","A"],["C","B"]]
#Output = "A"
class Solution:
    def destCity(self, paths):
        paths_table = {}
        for path in paths:
            start = path[0]
            to = path[1]
            paths_table[start] = to
        for value in paths_table.values():
            try:
                if not paths_table[value]:
                    return value
            except:
                return value

solution=Solution()

print(solution.destCity(paths))
print(solution.destCity(pathss))


        