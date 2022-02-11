# scores = [list(map(int, input().split())) for _ in range(5)]
# win_sum, winner = 0, 0
# for i, score in enumerate(scores):
#     if sum(score) > win_sum:
#         win_sum = sum(score)
#         winner = i + 1
# print(winner, win_sum, sep=' ')

scores = [list(map(int, input().split())) for _ in range(5)]
sum_score = [sum(score) for score in scores]
print(sum_score.index(max(sum_score)) + 1, max(sum_score))