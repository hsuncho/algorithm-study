n = int(input())
arr = [input() for _ in range(n)]

# Please write your code here.
m = max(len(x) for x in arr)
arr.sort(key = lambda x: x * 2 * m, reverse = True)
print(''.join(arr))