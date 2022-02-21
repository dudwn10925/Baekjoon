import sys
input = sys.stdin.readline
for _ in range(int(input().strip())):
    num, *scores = map(int, input().strip().split())
    mean_score = sum(scores) / len(scores)
    cnt = [s for s in scores if s > mean_score]
    ratio = (len(cnt) / len(scores)) *100
    print(f"{ratio:.3f}%")