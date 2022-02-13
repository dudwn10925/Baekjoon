# n = int(input())
# if (n >= 1) & (n <= 100):
#     for i in range(n):
#         if i % 2 == 0:
#             print("* " * n)
#         else:
#             print(" *" * n)
# else:
#     print('out of range')

n = int(input())
for i in range(n):
    print("* " * n if i % 2 ==0 else " *" * n)