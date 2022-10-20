from problem import Search
import copy, queue

def uniform_cost_search(problem):

    fila = queue.PriorityQueue()

    state = problem.getStartState()

    if problem.isGoalState(state):
        return []

    nodes_visitados = []

    while True:
        if fila.empty():
            state = (problem.getStartState(), [], 0)
        else:
            state = fila.get()
            print(state)

            if problem.isGoalState(state[0]):
                return state[1]

        if state[0] not in nodes_visitados:
            nodes_visitados.append(state[0])

            sucessores = problem.getSuccessors(state[0], state[2])

            for sucessor in sucessores:   
                passos_ate_sucessor = copy.deepcopy(state[1])
                passos_ate_sucessor.append(sucessor[1])

                coordenada_sucessor = sucessor[0][0] if len(str(sucessor[0])) > 15 else sucessor[0]

                fila.put((coordenada_sucessor, passos_ate_sucessor, state[2] + sucessor[2]))

  