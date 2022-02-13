# dial = {
#     'A': 3, 'B': 3, 'C': 3,
#     'D': 4, 'E': 4, 'F': 4,
#     'G': 5, 'H': 5, 'I': 5,
#     'J': 6, 'K': 6, 'L': 6,
#     'M': 7, 'N': 7, 'O': 7,
#     'P': 8, 'Q': 8, 'R': 8, 'S':8,
#     'T': 9, 'U': 9, 'V': 9,
#     'W': 10, 'X': 10, 'Y': 10, 'Z': 10
# }

# word = input()
# total = 0
# for w in word:
#     total += dial[w]
# print(total)

word = input()
dial = ["", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ", ""]
sum = 0
for w in word:
    for i, d in enumerate(dial):
        if w in d:
            i = i + 2
            sum += i
print(sum)