import collections


def lineEncoding(s):
    count = 1
    queue = collections.deque()
    answer = []
    for i in range(len(s)):
        if queue == collections.deque():
            queue.append(s[i])
        else:
            if queue[0] == s[i]:
                count += 1
            else:
                answer.append(str(count))
                answer.append(queue[0])

                queue.popleft()
                queue.append(s[i])
                count = 1

    answer.append(str(count))
    answer.append(queue[0])

    answer_str = ''.join([i for i in answer if i != "1"])
    return answer_str


print(lineEncoding("aabbbc"))  # 2a3bc
