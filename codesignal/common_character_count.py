import collections

def commonCharacterCount(s1, s2):
    s1 = collections.Counter(s1)
    s2 = collections.Counter(s2)

    s1_count = list(s1.items())
    
    answer = 0
    s2_keys = list(s2.keys())
    for i in range(len(s1_count)):
        s1_alpha = s1_count[i][0]

        if s1_alpha in s2_keys:

            s1_alpha_count = s1_count[i][1]
            s2_alpha_count = s2[s1_alpha]

            common = min(s1_alpha_count, s2_alpha_count)
            answer += common
    
    return answer

print(commonCharacterCount("aabcc", "adcaa"))
