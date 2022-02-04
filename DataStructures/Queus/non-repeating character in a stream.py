from queue import Queue

arr = 'ababe'

char_arr = [0] * 26
q = Queue(maxsize=0)
ans= ''
for i in arr:
    q.put(i)
    char_arr[ord(i) - ord('a')] += 1

    while (not q.empty()) :
        front = q.queue[0]
        if char_arr[ord(front) - ord('a')] <= 1:
            ans = ans + front
            break
        else:
            q.get_nowait()

    if q.empty():
        ans = ans + '#'

print(ans)
