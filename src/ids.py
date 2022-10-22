import queue

class IterativeDeepeningSearch:

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
            vizinhos.append(((coluna, linha-1), 'C'))

        if(linha != len(self.mapa)-1 and self.mapa[linha+1][coluna][0] != '@'):
            vizinhos.append(((coluna, linha+1), 'B'))
        
        if(coluna != 0 and self.mapa[linha][coluna-1][0] != '@'):
            vizinhos.append(((coluna-1, linha), 'E'))

        if(coluna != len(self.mapa[0])-1 and self.mapa[linha][coluna+1][0] != '@'):
            vizinhos.append(((coluna+1, linha), 'D'))
        
        return vizinhos

    def profundidade(self, estado):
        return len(estado[1])

    def depth_limited_search(self, limite):

        nodes_visitados = []
        pilha = queue.LifoQueue()
        estado = self.inicial   

        if self.eh_estado_objetivo(estado):
            return []    

        while True:

            if pilha.empty():
                estado = (self.inicial, [])
            else:
                estado = pilha.get()   

                if self.eh_estado_objetivo(estado[0]):
                    return estado[1]

                if limite < self.profundidade(estado):
                    return False

            if estado[0] not in nodes_visitados:
                nodes_visitados.append(estado[0])      
                vizinhos = self.get_vizinhos(estado[0])   

                for vizinho in vizinhos:   
                    passos_ate_vizinho = estado[1].copy()
                    passos_ate_vizinho.append(vizinho[1])
                    pilha.put((vizinho[0], passos_ate_vizinho)) 

    def iterative_deepening_search(self):
        result = False
        for i in range(2):
            while result == False:
                result = self.depth_limited_search(i)
        return result
