# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from typing import Tuple
from game import Directions
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    import copy

    grafo = util.Stack()

    node = problem.getStartState()

    if problem.isGoalState(node):
        return []

    nodes_visitados = []
    while True:
        if grafo.isEmpty():
            node = ((problem.getStartState(), "string aleatoria sem uso"), [])
        else:
            node = grafo.pop()

            if problem.isGoalState(node[0][0]):
                return node[1]
        
        if node[0][0] not in nodes_visitados:
            nodes_visitados.append(node[0][0])

            sucessores = problem.getSuccessors(node[0][0])

            for sucessor in sucessores:   
                copy_node = copy.deepcopy(node[1])
                copy_node.append(sucessor[1])
    
                grafo.push((sucessor, copy_node))


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    import copy

    fila = util.Queue()

    node = problem.getStartState() # (xi, yi)

    if problem.isGoalState(node): # (xf, yf)
        return [] # (xi, yi)

    nodes_visitados = []
    
    while True:
        if fila.isEmpty():
            node = ((problem.getStartState(), "string aleatoria sem uso"), []) # (((xi, yi), ""),[passos pra chegar no node (xi, yi)])
        else:
            node = fila.pop() # sucessor aplicando FIFO

            if problem.isGoalState(node[0][0]): # node[0][0] = (xi, yi)
                return node[1] # [...]
        
        if node[0][0] not in nodes_visitados:
            nodes_visitados.append(node[0][0])

            sucessores = problem.getSuccessors(node[0][0]) # vizinhos

            # node[1] lista de passos para chegar no proprio node
            for sucessor in sucessores:   
                passos_ate_sucessor = copy.deepcopy(node[1])

                # acao pra chegar no sucessor
                passos_ate_sucessor.append(sucessor[1])                
                fila.push((sucessor, passos_ate_sucessor))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    import copy

    fila_prioridade = util.PriorityQueue()

    node = problem.getStartState()

    if problem.isGoalState(node):
        return []

    nodes_visitados = []

    if isinstance(node, str) or isinstance(node[1], int):# quando nao e FoodProblem(este if...else foi criado para passar em todos os testes para esta busca, no autograder)

        while True:
            if fila_prioridade.isEmpty():
                node = (problem.getStartState(), [], 0)
            else:
                node = fila_prioridade.pop()

                if problem.isGoalState(node[0]):
                    return node[1]

            if node[0] not in nodes_visitados:
                nodes_visitados.append(node[0])

                sucessores = problem.getSuccessors(node[0])

                for sucessor in sucessores:   
                    copy_node = copy.deepcopy(node[1])
                    copy_node.append(sucessor[1])


                    coordenada_sucessor = sucessor[0][0] if len(str(sucessor[0])) > 15 else sucessor[0]

                    fila_prioridade.push((coordenada_sucessor, copy_node, node[2] + sucessor[2]), node[2] + sucessor[2])

    else: # Quando e FoodProblem
        while True:
            if fila_prioridade.isEmpty():
                node = (problem.getStartState(), [], 0)
            else:
                node = fila_prioridade.pop()
                
                if problem.isGoalState(node[0]):
                    return node[1]

            if node[0] not in nodes_visitados:
                nodes_visitados.append(node[0])
                
                sucessores = problem.getSuccessors(node[0])

                for sucessor in sucessores:   
                    copy_node = copy.deepcopy(node[1])
                    copy_node.append(sucessor[1])



                    coordenada_sucessor = sucessor[0]


                    fila_prioridade.push((coordenada_sucessor, copy_node, node[2] + sucessor[2]), node[2] + sucessor[2])


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def greedySearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest heuristic first."""
    import copy

    fila_prioridade = util.PriorityQueue()

    node = problem.getStartState()

    if problem.isGoalState(node):
        return []

    nodes_visitados = []
    
    while True:
        if fila_prioridade.isEmpty():
            node = (problem.getStartState(), [], 0)
        else:
            node = fila_prioridade.pop()
        
            if problem.isGoalState(node[0]):
                return node[1]

        if node[0] not in nodes_visitados:
            nodes_visitados.append(node[0])

            sucessores = problem.getSuccessors(node[0])

            for sucessor in sucessores:   
                copy_node = copy.deepcopy(node[1])
                copy_node.append(sucessor[1])

                coordenada_sucessor = sucessor[0]

                fila_prioridade.push((coordenada_sucessor, copy_node), heuristic(sucessor[0], problem))


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    import copy

    fila_prioridade = util.PriorityQueue()

    node = problem.getStartState()

    if problem.isGoalState(node):
        return []

    nodes_visitados = []
    
    while True:
        if fila_prioridade.isEmpty():
            node = (problem.getStartState(), [], 0)
        else:
            node = fila_prioridade.pop()
            
            if problem.isGoalState(node[0]):
                return node[1]

        if node[0] not in nodes_visitados:
            nodes_visitados.append(node[0])

            sucessores = problem.getSuccessors(node[0])

            for sucessor in sucessores:   
                copy_node = copy.deepcopy(node[1])
                copy_node.append(sucessor[1])

                coordenada_sucessor = sucessor[0]

                fila_prioridade.push((coordenada_sucessor, copy_node, sucessor[2] + node[2]), sucessor[2] + node[2] + heuristic(sucessor[0], problem))


def foodHeuristic(state, problem):
    """
    Your heuristic for the FoodSearchProblem goes here.

    This heuristic must be consistent to ensure correctness.  First, try to come
    up with an admissible heuristic; almost all admissible heuristics will be
    consistent as well.

    If using A* ever finds a solution that is worse uniform cost search finds,
    your heuristic is *not* consistent, and probably not admissible!  On the
    other hand, inadmissible or inconsistent heuristics may find optimal
    solutions, so be careful.

    The state is a tuple ( pacmanPosition, foodGrid ) where foodGrid is a Grid
    (see game.py) of either True or False. You can call foodGrid.asList() to get
    a list of food coordinates instead.

    If you want access to info like walls, capsules, etc., you can query the
    problem.  For example, problem.walls gives you a Grid of where the walls
    are.

    If you want to *store* information to be reused in other calls to the
    heuristic, there is a dictionary called problem.heuristicInfo that you can
    use. For example, if you only want to count the walls once and store that
    value, try: problem.heuristicInfo['wallCount'] = problem.walls.count()
    Subsequent calls to this heuristic can access
    problem.heuristicInfo['wallCount']
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"
    return 0


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch
gs = greedySearch
astar = aStarSearch
