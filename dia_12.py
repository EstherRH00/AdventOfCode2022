from queue import PriorityQueue
import numpy as np
import itertools
entrada = open("input_12b")
lines = entrada.readlines()
entrada.close()

mat = np.asarray([[lines[i][j] for j in range(len(lines[0])-1)]for i in range(len(lines))])
max_x, max_y = mat.shape
max_x -= 1
max_y -= 1
print(mat, max_x, max_y)


def gestiona_start(start):
    q = PriorityQueue()
    test_list = [range(max_x+1), range(max_y+1)]
    output_list = list(itertools.product(*test_list))

    visited = {p: None for p in output_list}
    q.put((0, start))
    solucio = float('inf')

    def get_cost(lletra):
        return ord(lletra) if lletra != "E" else ord("z")

    while not q.empty():
        #print("Itero")
        #print(visited)
        cost, coords = q.get()
        x, y = coords
        #print(cost, x, y, mat[x][y])
        if cost < solucio and (visited[coords] == None or visited[coords] > cost):
            visited[coords] = cost
            if mat[x][y] == "E":
                solucio = cost
            else:
                fills = []
                if x != 0:
                    if get_cost(mat[x-1][y]) <= ord(mat[x][y]) + 1:
                        fills.append((x-1, y))
                if y != 0:
                    if get_cost(mat[x][y-1]) <= ord(mat[x][y]) + 1:
                        fills.append((x, y-1))
                if x != max_x:
                    if get_cost(mat[x + 1][y]) <= ord(mat[x][y]) + 1:
                        fills.append((x+1, y))
                if y != max_y:
                    if get_cost(mat[x][y+1]) <= ord(mat[x][y]) + 1:
                        fills.append((x, y+1))
                #print(fills)
                for f in fills:
                    q.put((cost+1, f))

    #print("solucio", solucio)
    return solucio

ii = np.where(mat == "S")

start = (ii[0][0], ii[1][0])
mat[start[0]][start[1]] = "a"
print(start)
print("primera part", gestiona_start(start))


ii = np.where(mat == "a")
starts = [(ii[0][i], ii[1][i]) for i in range(len(ii[0]))]
best = float('inf')
for start in starts:
    s = gestiona_start(start)
    if best > s:
        best = s
print("the best", best)


