import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())

pokemon = {}
lst = []
for i in range(n+m):
    name = input().strip()
    if i < n:
        pokemon[name] = str(i+1)
        pokemon[str(i+1)] = name
    else:
        lst.append(pokemon[name])
for l in lst:
    print(l)
    
# for i in range(n):
#     name = input().strip()
#     pokemon[name] = str(i+1)
#     pokemon[str(i+1)] = name

# lst = []
# for _ in range(m):
#     monster = input().strip()
#     lst.append(pokemon[monster])

# for l in lst:
#     print(l)