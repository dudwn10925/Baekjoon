# word = input()
# result = str()
# if (len(word) > 2) & (len(word) < 101):
#     for w in word:
#         if w not in 'CAMBRIDGE':
#             result += w
# else:
#     print('out of range')
# print(result)

word = input()
for i in 'CAMBRIDGE':
    word = word.replace(i, "")
print(word)