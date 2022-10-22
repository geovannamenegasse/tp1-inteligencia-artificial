import queue

class GreedySearch:

    def __init__(self, inicial, objetivo, mapa):
        self.inicial = inicial
        self.objetivo = objetivo
        self.mapa = mapa

    def eh_estado_objetivo(self, estado):
        return estado == self.objetivo

    def get_vizinhos(self, estado):
        vizinhos = []

        linha = estado[1]
        coluna = estado[0]
     
        if(linha != 0 and self.mapa[linha-1][coluna][0] != '@'):
            vizinhos.append((0, (coluna, linha-1), 'C'))

        if(linha != len(self.mapa)-1 and self.mapa[linha+1][coluna][0] != '@'):
            vizinhos.append((0, (coluna, linha+1), 'B'))
        
        if(coluna != 0 and self.mapa[linha][coluna-1][0] != '@'):
            vizinhos.append((0, (coluna-1, linha), 'E'))

        if(coluna != len(self.mapa[0])-1 and self.mapa[linha][coluna+1][0] != '@'):
            vizinhos.append((0, (coluna+1, linha), 'D'))
        
        return vizinhos

    def heuristica(self, estado):
        return abs(estado[0]-self.objetivo[0])+abs(estado[1]-self.objetivo[1])

    def greedy_search(self):

        nodes_visitados = []
        fila = queue.PriorityQueue()
        estado = self.inicial

        if self.eh_estado_objetivo(estado):
            return []

        while True:
            if fila.empty():
                estado = (0, self.inicial, [])
            else:
                estado = fila.get()

                if self.eh_estado_objetivo(estado[1]):
                    return estado[2]

            if estado[1] not in nodes_visitados:
                nodes_visitados.append(estado[1])
                vizinhos = self.get_vizinhos(estado[1])

                for vizinho in vizinhos:   
                    passos_ate_vizinho = estado[2].copy()
                    passos_ate_vizinho.append(vizinho[2])
                    fila.put((self.heuristica(vizinho[1]), vizinho[1], passos_ate_vizinho))
