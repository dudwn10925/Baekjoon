result = []
for i in range(int(input())):
    a, b = map(int, input().split())
    if (a > 0) & (a < 10) & (b > 0) & (b < 10):
        result.append(f'Case #{i+1}: {a} + {b} = {a+b}')
    else:
        result.append(f'out of range')
print(*result, sep='\n')