

class Search:

    def __init__(self, start, goal, tuples):
        self.start = start
        self.goal = goal
        self.map = tuples

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        return self.start

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        return state == self.goal

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        # D = (state[0], state[1]+1)
        # C = (state[0]-1, state[1])
        # E = (state[0], state[1]-1)
        # B = (state[0]+1, state[1])

        # mD = None if(D[1] >= len(self.map[0])) else self.map[D[0]][D[1]]
        # mC = None if(C[0] < 0) else self.map[state[0]][state[1]+1]
        # mE = None if(E[1] < 0) else self.map[E[0]][E[1]]
        # mB = None if(B[0] >= len(self.map)) else self.map[B[0]][B[1]]

        successors = []

        linha = state[1]
        coluna = state[0]
     
        if(linha != 0):
            if(self.map[linha-1][coluna][0] != '@'):
                successors.append(((coluna, linha-1), 'C'))

        if(linha != len(self.map) - 1):
            if(self.map[linha+1][coluna][0] != '@'):
                successors.append(((coluna, linha+1), 'B'))
        
        if(coluna != 0):
            if(self.map[linha][coluna-1][0] != '@'):
                successors.append(((coluna-1, linha), 'E'))

        if(coluna != len(self.map[0]) - 1):
            if(self.map[linha][coluna+1][0] != '@'):
                successors.append(((coluna+1, linha), 'D'))
        

        return successors



class SearchUCS:

    def __init__(self, start, goal, tuples):
        self.start = start
        self.goal = goal
        self.map = tuples

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        return self.start

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        return state == self.goal

    def getSuccessors(self, state, cost):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        # D = (state[0], state[1]+1)
        # C = (state[0]-1, state[1])
        # E = (state[0], state[1]-1)
        # B = (state[0]+1, state[1])

        # mD = None if(D[1] >= len(self.map[0])) else self.map[D[0]][D[1]]
        # mC = None if(C[0] < 0) else self.map[state[0]][state[1]+1]
        # mE = None if(E[1] < 0) else self.map[E[0]][E[1]]
        # mB = None if(B[0] >= len(self.map)) else self.map[B[0]][B[1]]

        successors = []

        linha = state[1]
        coluna = state[0]
     
        if(linha != 0):
            if(self.map[linha-1][coluna][0] != '@'):
                successors.append(((coluna, linha-1), 'C', cost))

        if(linha != len(self.map) - 1):
            if(self.map[linha+1][coluna][0] != '@'):
                successors.append(((coluna, linha+1), 'B', cost))
        
        if(coluna != 0):
            if(self.map[linha][coluna-1][0] != '@'):
                successors.append(((coluna-1, linha), 'E', cost))

        if(coluna != len(self.map[0]) - 1):
            if(self.map[linha][coluna+1][0] != '@'):
                successors.append(((coluna+1, linha), 'D', cost))
        

        return successors



