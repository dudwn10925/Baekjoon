n, m = map(int, input().split())
pokemon = {}
for i in range(n):
    monster = input()
    pokemon[f'{i+1}'] = monster
    pokemon[monster] = f"{i+1}"

result = []
for i in range(m):
    monster = input()
    result.append(pokemon[monster])
    
for r in result:
    print(r)