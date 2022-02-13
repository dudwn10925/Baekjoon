# import sys
# input = sys.stdin.readline
# result = []
# for _ in range(int(input())):
#     num, word = input().strip().split()
#     new_word = ""
#     for w in word:
#         for _ in range(int(num)):
#             new_word += w
#     result.append(new_word)
# for r in result:
#     print(r)

result = []
for _ in range(int(input())):
    num, word = input().strip().split()
    new_word = ''
    for w in word:
        new_word += w * int(num)
    result.append(new_word)
for r in result:
    print(r)