N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
ratio = [(value / weight, i) for i, (value, weight) in enumerate(zip(v, w))]
ratio.sort(key=lambda x:x[0], reverse = True)

result = 0
bag = 0
for r in ratio:
    if bag + w[r[1]] > M:
        result += ((M - bag) / w[r[1]]) * v[r[1]]
        break
    else:
        bag += w[r[1]]
        result += v[r[1]]
print(f"{result:.3f}")
