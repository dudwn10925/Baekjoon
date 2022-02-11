# board = [list(input()) for _ in range(8)]
# cnt = 0
# for i, row in enumerate(board):
#     if i % 2 == 0:
#         for j, dot in enumerate(row):
#             if (j % 2 == 0) & (dot == 'F'):
#                 cnt += 1
#     else:
#         for j, dot in enumerate(row):
#             if (j % 2 == 1) & (dot == 'F'):
#                 cnt += 1
# print(cnt)

board = [input() for _ in range(8)]
cnt = 0
for i, row in enumerate(board):    
    row = row[::2] if i % 2 == 0 else row[1::2]
    cnt += row.count('F')
    a = row
print(cnt)

# 가로가 아닌 세로로 탐색해보기

# board = [list(input()) for _ in range(8)]
# total = 0
# for i in range(8):
#     for i in range(8):
#         if i % 2 == i % 2 and board[i][i] == 'F':
#             total += 1
# print(total)