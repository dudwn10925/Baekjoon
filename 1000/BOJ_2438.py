n = int(input())
if (n >= 1) & (n <=100):
    for i in range(n):
        print('*' * (i+1))
else:
    print('out of range')