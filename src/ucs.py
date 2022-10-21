import copy, queue

class UniformCostSearch:

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
            successors.append(((coluna, linha-1), 'C', self.map[state[1]][state[0]][1]))

        if(linha != len(self.map) - 1 and self.map[linha+1][coluna][0] != '@'):
            successors.append(((coluna, linha+1), 'B', self.map[state[1]][state[0]][1]))
        
        if(coluna != 0 and self.map[linha][coluna-1][0] != '@'):
            successors.append(((coluna-1, linha), 'E', self.map[state[1]][state[0]][1]))

        if(coluna != len(self.map[0]) - 1 and self.map[linha][coluna+1][0] != '@'):
            successors.append(((coluna+1, linha), 'D', self.map[state[1]][state[0]][1]))
        

        return successors

    def uniform_cost_search(self):

        fila = queue.PriorityQueue()

        state = self.get_start_state()

        if self.is_goal_state(state):
            return []

        nodes_visitados = []

        while True:
            if fila.empty():
                state = (self.get_start_state(), [], self.map[self.get_start_state()[1]][self.get_start_state()[0]][1])
            else:
                state = fila.get()

                if self.is_goal_state(state[0]):
                    return state[1]

            if state[0] not in nodes_visitados:
                nodes_visitados.append(state[0])

                sucessores = self.get_successors(state[0])

                for sucessor in sucessores:   
                    passos_ate_sucessor = copy.deepcopy(state[1])
                    passos_ate_sucessor.append(sucessor[1])

                    coordenada_sucessor = sucessor[0][0] if len(str(sucessor[0])) > 15 else sucessor[0]

                    fila.put((coordenada_sucessor, passos_ate_sucessor, state[2] + sucessor[2]))

    