import sys
N, M = map(int, sys.stdin.readline().split())
pokedex = {}
for i in range(1, N+1):
    pokemon = sys.stdin.readline().strip()
    pokedex[str(i)] = pokemon
    pokedex[pokemon] = str(i)
for i in range(M):
    print(pokedex.get(sys.stdin.readline().strip()))