from search import *
import matplotlib.pyplot as plt


h = {'S':7, 'A':1, 'B':2, 'C':6, 'G':0} ## simple heuristics according to slides

if __name__ == "__main__":
    ## Romania
    connections = [('A', 'S', 140), ('A', 'Z', 75), ('A', 'T', 118), ('C', 'P', 138), ('C', 'R', 146), ('C', 'D', 120), ('B', 'P', 101),
                   ('B', 'U', 85), ('B', 'G', 90), ('B', 'F', 211), ('E', 'H', 86), ('D', 'M', 75), ('F', 'S', 99), ('I', 'V', 92),
                   ('I', 'N', 87), ('H', 'U', 98), ('L', 'M', 70), ('L', 'T', 111), ('O', 'S', 151), ('O', 'Z', 71), ('P', 'R', 97), ('R', 'S', 80), ('U', 'V', 142)]
    
    locations =     {'A': (91, 492), 'C': (253, 288), 'B': (400, 327), 'E': (562, 293), 'D': (165, 299), 'G': (375, 270), 'F': (305, 449),
                     'I': (473, 506), 'H': (534, 350), 'M': (168, 339), 'L': (165, 379), 'O': (131, 571), 'N': (406, 537), 'P': (320, 368),
                     'S': (207, 457), 'R': (233, 410), 'U': (456, 350), 'T': (94, 410), 'V': (509, 444), 'Z': (108, 531)}


    romania = NavigationProblem('A', 'B', connections) ## for A*, you will need to also provide the locations
    
    print (romania.successors('A')) ## [('go to S', 140, 'S'), ('go to Z', 75, 'Z'), ('go to T', 118, 'T')]
    solution, history = breadth_first_graph_search(romania)
    print ([(node.state, node.action) for node in solution.getPath()])
    

    # TODO: apply UCS, Greedy search and A*, the heuristic being the Euclidean 
    

    nx.draw(romania.graph)
    plt.show()

    
