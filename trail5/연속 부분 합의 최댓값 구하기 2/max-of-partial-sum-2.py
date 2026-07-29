n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
ans = max(a)
result = 0
for i in range(n):
    result += a[i]
    if result < 0:
        result = 0
        continue
    ans = max(ans, result)
print(ans)