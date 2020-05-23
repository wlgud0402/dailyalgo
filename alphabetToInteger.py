table = {
    "1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h","9":"i",
    "10":"j","11":"k","12":"l","13":"m","14":"n","15":"o","16":"p","17":"q",
    "18":"r","19":"s","20":"t","21":"u","22":"v","23":"w","24":"x","25":"y","26":"z"
}

class Solution:
    def freqAlphabets(self, string):
        result =[]
        for i in range(len(string), 0 , -1):
            if string[i] == "#":
                print("hi")
                s = string[i-2] + string[i-1]
                result.append(table[s])
            else:
                s = string[i]
                result.append(table[s])
        result.reverse()
        return result

solution=Solution()

print(solution.freqAlphabets("1326#"))
                