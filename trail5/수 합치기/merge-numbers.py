import heapq
n= int(input())
arr = list(map(int, input().split()))

# Please write your code here.
heapq.heapify(arr)
cost = 0
while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    s = a + b
    cost += s
    heapq.heappush(arr, s)
print(cost)