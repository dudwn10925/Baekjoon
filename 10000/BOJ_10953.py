result = []
for _ in range(int(input())):
    a, b = map(int, input().split(','))
    if (a > 0) & (a < 10) & (b > 0) & (b < 10):
        result.append(a + b)
    else:
        result.append('out of range')
print(*result, sep='\n')