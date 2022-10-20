import copy
import queue

def breadth_first_search(problem):
    """Search the shallowest nodes in the search tree first."""
    
    fila = queue.Queue()

    state = problem.getStartState() # (xi, yi)

    if problem.isGoalState(state): # (xf, yf)
        return [] # (xi, yi)

    nodes_visitados = []
    
    while True:
        if fila.empty():
            state = (problem.getStartState(), []) # (((xi, yi), ""),[passos pra chegar no node (xi, yi)])
        else:
            state = fila.get() # sucessor aplicando FIFO

            if problem.isGoalState(state[0]): # node[0][0] = (xi, yi)
                return state[1] # [...]
        
        if state[0] not in nodes_visitados:
            nodes_visitados.append(state[0])
            
            sucessores = problem.getSuccessors(state[0]) # vizinhos
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

    
    