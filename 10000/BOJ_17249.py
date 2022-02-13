# def taebo_func(to, taebo):
#     cnt = 0
#     if to == 1:
#         taebo = taebo[::-1]
#     for tb in taebo:
#         if tb == '@':
#             cnt += 1
#         if (tb == '(') | (tb == ')'):
#             break
#     return cnt

# in_taebo = input()
# print(taebo_func(0, in_taebo), taebo_func(1, in_taebo))

# taebo = input()
# left_tb, right_tb = taebo.split('(')
# print(left_tb.count('@'), right_tb.count('@'))

left, right = input().split("0")
print(left.count('@'), right.count('@'))