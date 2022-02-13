result = []
for i in range(int(input())):
    a, b = map(int, input().split())
    result.append(f'Case #{i+1}: {a+b}')
print(*result, sep='\n')