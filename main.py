import sys
from bfs import breadth_first_search
from ucs import uniform_cost_search
from problem import Search, SearchUCS

arquivo = open(sys.argv[1], 'r')

metodo = sys.argv[2]
# print(metodo)

pi = (ci, li) = (int(sys.argv[3]), int(sys.argv[4]))
pf = (cf, lf) = (int(sys.argv[5]), int(sys.argv[6]))

# print(pi)
# print(pf)

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

# print(tuplas)
arquivo.close()

problem = Search(pi, pf, tuplas)

if metodo == "bfs":
    path = breadth_first_search(problem)
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

if metodo == "ucs":
    problem = SearchUCS(pi, pf, tuplas)

    path = uniform_cost_search(problem)
    print(path)