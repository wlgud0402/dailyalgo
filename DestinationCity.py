class Solution:
    def destCity(self, paths):
        destination = {}
        if len(paths) == 1:
            return paths[0][1]

        for path in paths:
            destination[path[0]] = path[1]

        for path in paths:
            try:
                if destination[path[1]]:
                    continue
            except:
                return path[1]

solution = Solution()
print(solution.destCity([["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]))