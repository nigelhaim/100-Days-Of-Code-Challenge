nodes  = int(input("Number of Nodes: "))
edges = nodes + 1

matrix = [[0 for x in range(nodes)] for y in range(nodes)] 

for setEdge in range(edges):
    i = int(input("Enter source vertex: "))
    j = int(input("Enter destination vertex: "))

    matrix [i][j] = 1
    matrix [j][i] = 1


for n in matrix:
    for m in n:
        print(m, end = " ")
    print()


