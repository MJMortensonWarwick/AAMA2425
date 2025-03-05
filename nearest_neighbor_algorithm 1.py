

import pandas as pd
import time 

start = time.time()

df = pd.read_excel('real_distances_40customers.xls', index_col=0) # dataframe

df.describe() # some descriptive stats

df.info() # summary info

df.shape # number of rows & columns

df.columns # list of column names

nodes = list(range(df.shape[0]))# List of nodes
nodes

d = [[df[j][i] for j in nodes] for i in nodes]# Build distance matrix



print('distance matrix:', d)

origin = 0 

tour = [origin]
print('tour is:', tour)

print('current lenght of the tour:', len(tour))

print('numober of nodes is:', len(nodes))

tour_length = 0

current_node = origin

current_node

while len(tour) < len(nodes):
    nearest_node = None # not known yet
    dist_to_nearest_node = max(d[current_node])+1 # a large enough number
    # Find the (unvisited) node that is nearest with respect to the current node
    for i in nodes:
        if i not in tour and d[current_node][i] < dist_to_nearest_node:
            print("Node", i, "is closer to", current_node, "with distance", d[current_node][i])
            nearest_node = i # update nearest node
            dist_to_nearest_node = d[current_node][i] # update distance to nearest node
    print("The nearest unvisited node is found to be", nearest_node)
    tour_length += dist_to_nearest_node # update the tour length
    tour.append(nearest_node) # add the nearest node to the end of the tour
    print('Added', nearest_node, 'to the tour!')
    current_node = nearest_node # update the current node

print('final tour is:', tour)

print('lenght of the tour is:', tour_length)

print('TSP tour found with nearest neighbor search starting from', origin, 
          'is', tour, 'with total length', tour_length)

print(time.time() - start)