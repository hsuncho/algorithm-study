n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
meetings.sort(key = lambda x: x[1])
cnt = 1
end = meetings[0][1]
for s, e in meetings[1:]:
    if s >= end:
        cnt += 1
        end = e
    else:
        continue
print(cnt)