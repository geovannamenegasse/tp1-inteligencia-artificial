import sys

arquivo = open(sys.argv[1], 'r')

metodo = sys.argv[2]
print(metodo)

pi = (xi, yi) = (int(sys.argv[3]), int(sys.argv[4]))
pf = (xf, yf) = (int(sys.argv[5]), int(sys.argv[6]))

print(pi)
print(pf)

costs = {
    '.' : 1.0,
    ';' : 1.5,
    '+' : 2.5,
    'x' : 6.0,
    '@' : float('inf')
}

wh = arquivo.readline()
w = int(wh[0])
h = int(wh[2])

tuplas = []

for i in range(h):
    linha = []
    for j in range(w+1):
        char = arquivo.read(1)
        if char != '\n' and char != '':
            linha.append((char, costs[char]))
    tuplas.append(linha)

print(tuplas)

arquivo.close()
