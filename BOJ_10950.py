T = int(input())
result = []
for _ in range(T):
    a, b = map(int, input().split())
    result.append(a + b)
print(*result, sep='\n')