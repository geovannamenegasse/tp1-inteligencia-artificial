import copy, queue

class BreadthFirstSearch:

    def __init__(self, start, goal, tuples):
        self.start = start
        self.goal = goal
        self.map = tuples

    def get_start_state(self):
        return self.start

    def is_goal_state(self, state):
        return state == self.goal

    def get_successors(self, state):

        successors = []

        linha = state[1]
        coluna = state[0]
     
        if(linha != 0 and self.map[linha-1][coluna][0] != '@'):
            successors.append(((coluna, linha-1), 'C'))

        if(linha != len(self.map) - 1 and self.map[linha+1][coluna][0] != '@'):
            successors.append(((coluna, linha+1), 'B'))
        
        if(coluna != 0 and self.map[linha][coluna-1][0] != '@'):
            successors.append(((coluna-1, linha), 'E'))

        if(coluna != len(self.map[0]) - 1 and self.map[linha][coluna+1][0] != '@'):
             successors.append(((coluna+1, linha), 'D'))
        

        return successors

    def breadth_first_search(self):
        """Search the shallowest nodes in the search tree first."""

        fila = queue.Queue()

        state = self.get_start_state() # (xi, yi)

        if self.is_goal_state(state): # (xf, yf)
            return [] # (xi, yi)

        nodes_visitados = []

        while True:
            if fila.empty():
                state = (self.get_start_state(), []) # (((xi, yi), ""),[passos pra chegar no node (xi, yi)])
            else:
                state = fila.get() # sucessor aplicando FIFO

                if self.is_goal_state(state[0]): # node[0][0] = (xi, yi)
                    return state[1] # [...]

            if state[0] not in nodes_visitados:
                nodes_visitados.append(state[0])

                sucessores = self.get_successors(state[0]) # vizinhos
                # print(sucessores)
                # node[1] lista de passos para chegar no proprio node
                for sucessor in sucessores:   
                    # print(sucessor)
                    passos_ate_sucessor = copy.deepcopy(state[1])

                    # acao pra chegar no sucessor
                    passos_ate_sucessor.append(sucessor[1])                
                    fila.put((sucessor[0], passos_ate_sucessor))
                    # print((sucessor, passos_ate_sucessor))
                # print("")


