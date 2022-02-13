# n = int(input())
# if (n >= 1) & (n <=100):
#     for i in range(n):
#         print(f"{'*'*(i+1):>{n}}")
# else:
#     print('out of range')

n = int(input())
for i in range(n):
    print(" " * (n-i-1) + '*' * (i+1))