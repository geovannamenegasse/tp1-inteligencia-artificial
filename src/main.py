import time
start_time = time.time()

import sys

from bfs import BreadthFirstSearch
from ucs import UniformCostSearch
from greedy import GreedySearch
from astar import AStarSearch
from ids import IterativeDeepeningSearch

################################################################

arquivo = open(sys.argv[1], 'r')
metodo = sys.argv[2]
pi = (ci, li) = (int(sys.argv[3]), int(sys.argv[4]))
pf = (cf, lf) = (int(sys.argv[5]), int(sys.argv[6]))

costs = {
    '.' : 1.0,
    ';' : 1.5,
    '+' : 2.5,
    'x' : 6.0,
    '@' : float('inf')
}

wh = arquivo.readline().split(" ")
w = int(wh[0])
h = int(wh[1])

tuplas = []

for i in range(h):
    linha = []
    for j in range(w+1):
        char = arquivo.read(1)
        if char != '\n' and char != '':
            linha.append((char, costs[char]))
    tuplas.append(linha)

arquivo.close()
search_problem = None
caminho = []

if metodo == "BFS":
    search_problem = BreadthFirstSearch(pi, pf, tuplas)
    caminho = search_problem.breadth_first_search()

if metodo == "UCS":
    search_problem = UniformCostSearch(pi, pf, tuplas)
    caminho = search_problem.uniform_cost_search()

if metodo == "Greedy":
    search_problem = GreedySearch(pi, pf, tuplas)
    caminho = search_problem.greedy_search()

if metodo == "Astar":
    search_problem = AStarSearch(pi, pf, tuplas)
    caminho = search_problem.a_star_search()

if metodo == "IDS":
    search_problem = IterativeDeepeningSearch(pi, pf, tuplas)
    caminho = search_problem.iterative_deepening_search()

# print(path)

custo_total = 0
indices_caminho = []

for direction in caminho:
    if direction == 'D':
        ci += 1
    if direction == 'C':
        li -= 1
    if direction == 'E':
        ci -= 1
    if direction == 'B':
        li += 1
    indices_caminho.append((ci,li))
    custo_total += search_problem.mapa[li][ci][1]

print(custo_total, end=" ")

print(pi, end=" ")
for p in indices_caminho:
    print(p, end=" ")
print("\n")
print(len(indices_caminho))

print("--- %s seconds ---" % (time.time() - start_time))
