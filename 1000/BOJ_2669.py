# import numpy as np
# board = np.zeros((100, 100))
# coord = [list(map(int, input().split())) for _ in range(4)]

# for i in range(4):
#     for x in range(coord[i][0], coord[i][2]):
#         for y in range(coord[i][1], coord[i][3]):
#             board[x, y] = 1
# print(int(np.sum(board)))

board = [[0] * 100 for _ in range(100)]
coord = [list(map(int, input().split())) for _ in range(4)]

for i in range(4):
    for x in range(coord[i][0], coord[i][2]):
        for y in range(coord[i][1], coord[i][3]):
            board[x][y] = 1
print(sum(sum(line) for line in board))