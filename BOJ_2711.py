# for _ in range(int(input())):
#     result = ""
#     loc, word = input().split()
#     for i, _ in enumerate(word):
#         if i == int(loc) - 1:
#             continue
#         else:
#             result += word[i]
#     print(result)

for _ in range(int(input())):
    index, word = input().split()
    index = int(index)
    print(word[:index-1] + word[index:])