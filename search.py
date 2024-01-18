import networkx as nx
import numpy as np
import bisect
import random

from romania import *

class NavigationProblem:
    def __init__(self, initial, goal, connections, locations=None, directed=False):
        self.initial = initial
        self.goal = goal
        self.locations = locations
        self.graph = nx.DiGraph() if directed else nx.Graph()
        for cityA, cityB, distance in connections:
            self.graph.add_edge(cityA, cityB, cost=distance)            
    def successors(self, state):
        ## Exactly as defined in Lecture slides, 
        return [("go to %s" % city, connection['cost'], city) for city, connection in self.graph[state].items()]
    def goal_test(self, state):
        return state == self.goal

class PuzzleState:
    def __init__(self, matrix=None, goal=False, init=False, size=3):
        ## ** add code that generates puzzle states of varying difficulty
        self.size = size
        if not matrix is None: ## 0 represents empty spot
            self.matrix = matrix
        else: ## defining init or goal state
            ## this is too hard for the benchmark, change this!
            ## *** Your code here ***
            permutation = np.array(range(size*size))
            if init:
                random.shuffle(permutation) 
            self.matrix = permutation.reshape((size, size))
    def successors(self):
        pass
        ## TODO 
        ## *** Your code here ***
        ## return a list of successors
        ## each successor is a tuple of 
        ## 1. a string, describing the action, 
        ## 2. action cost (here 1), 
        ## 3. and the new state

    def __hash__(self):
        pass
        ## return a hash code, if you have a matrix, you can uncomment this:
        #return hash(tuple(self.matrix.flatten()))
    def __eq__(self, other):
        pass
        ## this function defines equality between objects, if you have a matrix, you can uncomment this:
        ##return np.alltrue(other.matrix == self.matrix)

class PuzzleProblem:
    def __init__(self, size=3): #size 3 means 3x3 field
        self.size = size        
        self.initial = PuzzleState(init=True, size=size)  ## init state is shuffled 
        self.goal = PuzzleState(goal=True, size=size)  ## goal state is unshuffled 
    def successors(self, state):
        return state.successors()
        ## Successors can be "outsourced", you can also calculate successor states here
    def goal_test(self, state):
        # *** your code here ***
        return False ## change this as appropriate!!

class Node:
    def __init__(self, state=None, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost        
    def getPath(self):
        """getting the path of parents up to the root"""
        currentNode = self
        path = [self]
        while currentNode.parent: ## stops when parent is None, ie root
            path.append(currentNode.parent)
            currentNode = currentNode.parent
        path.reverse() #from root to this node
        return path
    def expand(self, problem):
        successors = problem.successors(self.state)
        return [Node(newState, self, action, self.path_cost+cost) for (action, cost, newState) in successors]
    def __gt__(self, other): ## needed for tie breaks in priority queues
        return True
    def __repr__(self):
        return (self.state, self.action, self.path_cost)
    
class FIFO:
    def __init__(self):
        self.list = []
    def push(self, item):
        self.list.insert(0, item)  
    def pop(self):
        return self.list.pop()
class LIFO:  ## TODO: fill out yourself! 
    def __init__(self):
        pass
    def push(self, item):
        pass
    def pop(self):
        pass
class PriorityQueue:
    def __init__(self, f):
        self.list = []
        self.f = f
    def push(self, item):
        priority = self.f(item)
        bisect.insort(self.list, (priority, random.random(), item))
    def pop(self):
        return self.list.pop(0)[-1]
        
def graph_search(problem, frontier):
    """Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    If two paths reach a state, only use the best one. [Fig. 3.18]"""
    closed = set() ## sets can store hashable objects, thats why we need to define a hash code for states
    frontier.push(Node(problem.initial))
    explorationHistory = []
    while frontier:
        pass
        # TODO 
        # *** your code here ***

    
def breadth_first_graph_search(problem):
    return graph_search(problem, FIFO())
def depth_first_graph_search(problem):
    return graph_search(problem, LIFO())
def astar_graph_search(problem, f):
    return graph_search(problem, PriorityQueue(f))

#%%
# priority functions for Priority Queues used in UCS and A*, resp., if you are unfamiliar with lambda calc.

def ucs(node):
    return node.path_cost

def f(node):
    return node.path_cost + h[node.state]

if __name__ == "__main__":
    ## Getting familiar with the Toy NavigationProblem
    toyConnections = [('S', 'A', 5), ('S', 'B', 3), ('S', 'C', 1), ('A', 'G', 1), ('B', 'G', 2), ('C', 'G', 17)]
    h = {'S':7, 'A':1, 'B':2, 'C':6, 'G':0} ## simple heuristics according to slides
    
    toy = NavigationProblem('S', 'G', toyConnections, directed=True)
    # Uniform cost:
    sol, history = graph_search(toy, PriorityQueue(ucs))
    print ("UCS Solution:", [(node.state, node.action) for node in sol.getPath()])
    print ("exploration history:", [node.state for node in history])

#%%
    # Best first
    sol, history = graph_search(toy, PriorityQueue(lambda node: h[node.state]))
    print ("Greedy Search Solution:", [(node.state, node.action) for node in sol.getPath()])
    print ("exploration history:", [node.state for node in history])
#%%
    # A*
    sol, history = graph_search(toy, PriorityQueue(f))
    print ("A* Solution:", [(node.state, node.action) for node in sol.getPath()])
    print ("exploration history:", [node.state for node in history])

#%%
