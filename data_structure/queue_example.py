from collections import deque

if __name__ == "__main__":
    q = deque([1,2,3])
    front = q.popleft()
    end = q.pop()
    q.append(4)
    q.appendleft(5)
    for x in q:
        print(x)
