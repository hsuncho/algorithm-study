n = int(input())

# Please write your code here.
cnt = 0
while n > 0:
    if n % 5 != 0:
        n -= 2
        cnt += 1
    else:
        cnt += n // 5
        n %= 5
print(cnt if n == 0 else -1)
