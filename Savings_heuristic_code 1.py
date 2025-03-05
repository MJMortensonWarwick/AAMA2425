import pandas as pd

df = pd.read_excel('real_distances_10customers.xls', index_col=0)

df

nodes = list(range(df.shape[0]))
nodes

d = [[round(float(df[j][i]), 2) for j in nodes] for i in nodes]

d

d2 = df.values.tolist()
d2

origin = 0

customers = {i for i in nodes if i != origin}
customers

tours = {(i,i): [origin, i, origin] for i in customers}
tours

savings = {(i, j): round(d[i][origin] + d[origin][j] - d[i][j], 2) 
           for i in customers for j in customers if j != i}

savings

sorted_savings = sorted(savings.items(), key=lambda item: item[1])

tours

len(tours)

while len(tours) > 1:
    A = sorted_savings.pop()
    i = A[0][0]
    j = A[0][1]
    print((i, j))
    # Outer loop
    break_outer = False
    for t1 in tours:
        for t2 in tours.keys()-{t1}:
            if t1[1] == i and t2[0] == j:
                print('Merging', tours[t1], 'and', tours[t2])
                tours[(t1[0], t2[1])] = tours[t1][:-1] + tours[t2][1:]
                del tours[t1], tours[t2]
                print(tours)
                break_outer = True
                break
        if break_outer:
            break
    else:
        print('No merging opportunities can be found for', (i,j)) 

print(tours)

tour_length = 0
for tour in tours.values():
    for i in range(len(tour)-1):
        tour_length += d[tour[i]][tour[i+1]]

tour_length = round(tour_length, 2)

print('TSP tour found with savings heuristic starting from', origin, 'is', tour, 'with total length', tour_length)

