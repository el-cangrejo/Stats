import random as rnd
import math
import matplotlib.pyplot as plt

if __name__ == "__main__":
    graph_size = 51
    number_of_simulations = 10001
    number_of_iterations = 100 
    graph = []
    
    for i in range(graph_size):
        graph.append(0)

    for i in range(number_of_simulations):
        index = math.floor(graph_size / 2)
#        if rnd.random() >= 0.0:
            number_of_iterations = 100
#        else:
#            number_of_iterations = 101
        for j in range(number_of_iterations):
            if rnd.random() >= 0.5:
                if index < graph_size - 1:
                        next_index = index + 1
                else:
                        next_index = 0
            else:
                if index > 0:
                        next_index = index - 1
                else:
                        next_index = graph_size -1 
            index = next_index
        graph[int(next_index)] = graph[int(next_index)] + 1

    for i in range(graph_size):
        graph[i] = (graph[i] / float(number_of_simulations))

    print graph

    plt.plot(range(0,graph_size), graph)
    plt.show()
