# a, b = map(int, input().split())
# c = int(input())
# min = b + c
# while min >= 60:
#     min -= 60
#     a += 1
# if a >= 24:
#     a -= 24
# print(a, min)

a, b = map(int, input().split())
c = int(input())
print((a+(b+c)//60)%24, (b+c)%60)

# a, b = map(int, input().split())
# n = int(input()) + b + a*60
# print(n//60%24, n%60)