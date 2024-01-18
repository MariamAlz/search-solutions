from search import *
#from search_sol import *

class VacuumState:
    def __init__(self, dirtDistribution, robotPosition):
        self.dirtDistribution = dirtDistribution
        self.robotPosition = robotPosition
    def __repr__(self):
        return "[%s]" % "|".join(["%s%s"%(d, "*" if roomNr==self.robotPosition else " ") for roomNr, d in enumerate(self.dirtDistribution)])
    def __hash__(self):
        return hash(tuple(self.dirtDistribution + [self.robotPosition]))
    def __eq__(self, other):
        return self.dirtDistribution == other.dirtDistribution and self.robotPosition == other.robotPosition
    
class VacuumProblem:    ## Deterministic, Fully observable
    def __init__(self, initial):
        self.initial=initial
    def successors(self, state):
        actions = []
        if state.robotPosition < len(state.dirtDistribution)-1:
            actions.append(("goRight", 1, VacuumState(state.dirtDistribution, state.robotPosition+1)))
        if state.robotPosition > 0:
            actions.append(("goLeft", 1, VacuumState(state.dirtDistribution, state.robotPosition-1)))        
        if state.dirtDistribution[state.robotPosition] > 0: ## current position dirty
            dirt = state.dirtDistribution[:]
            dirt[state.robotPosition] = 0
            actions.append(("suck", 1, VacuumState(dirt, state.robotPosition)))
        return actions
    def goal_test(self, state):
        return sum(state.dirtDistribution) == 0

if __name__ == "__main__":
    vacuum = VacuumProblem(VacuumState([1,0,0,1,0,1], 3))
    ## make sure, graph search keeps track of a history!
    finalNode, history = graph_search(vacuum, FIFO())
    for node in finalNode.getPath():
        print(node.state, node.action)
    print("Explored States:", len(history))
# [1 |0 |0 |1*|0 |1 ] None
# [1 |0 |0 |1 |0*|1 ] goRight
# [1 |0 |0 |1 |0 |1*] goRight
# [1 |0 |0 |1 |0 |0*] suck
# [1 |0 |0 |1 |0*|0 ] goLeft
# [1 |0 |0 |1*|0 |0 ] goLeft
# [1 |0 |0 |0*|0 |0 ] suck
# [1 |0 |0*|0 |0 |0 ] goLeft
# [1 |0*|0 |0 |0 |0 ] goLeft
# [1*|0 |0 |0 |0 |0 ] goLeft
# [0*|0 |0 |0 |0 |0 ] suck
# Explored States: 67

