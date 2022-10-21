import sys

from bfs import BreadthFirstSearch
from ucs import UniformCostSearch
from greedy import GreedySearch
from astar import AStarSearch

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
problem = None
path = []

if metodo == "BFS":
    problem = BreadthFirstSearch(pi, pf, tuplas)
    path = problem.breadth_first_search()

if metodo == "UCS":
    problem = UniformCostSearch(pi, pf, tuplas)
    path = problem.uniform_cost_search()

if metodo == "Greedy":
    problem = GreedySearch(pi, pf, tuplas)
    path = problem.greedy_search()

if metodo == "Astar":
    problem = AStarSearch(pi, pf, tuplas)
    path = problem.a_star_search()

if metodo == "IDS":
    print("IDS")


# print(path)

cost = 0
path_inds = []

for direction in path:
    if direction == 'D':
        ci += 1
    if direction == 'C':
        li -= 1
    if direction == 'E':
        ci -= 1
    if direction == 'B':
        li += 1
    path_inds.append((ci,li))
    cost += problem.map[li][ci][1]

print(cost, end=" ")

for p in path_inds:
    print(p, end=" ")