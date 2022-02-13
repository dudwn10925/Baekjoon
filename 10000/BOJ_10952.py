result = []
while(1):
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        break
    result.append(a + b)
print(*result, sep='\n')