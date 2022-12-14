import numpy as np

entrada = open("input_14")
lines = entrada.readlines()
entrada.close()

def posa_terra(a, b, c, d, m):
    print("posant terra",a,b,c,d)
    if a == c:
        for i in range(min(d, b), max(d, b)+1):
            m[a][i] = 2
    else:
        for i in range(min(a, c), max(a,c)+1):
            m[i][b] = 2

def posa_arena(m):
    coords = [0, 500]
    block = False

    while not block:
        if coords[0] == 599:
            return True
        if mat[coords[0]+1, coords[1]] == 0:
            coords[0] += 1
        elif mat[coords[0]+1, coords[1]-1] == 0:
            coords[0] += 1
            coords[1] -= 1
        elif mat[coords[0]+1, coords[1]+1] == 0:
            coords[0] += 1
            coords[1] += 1
        else: block = True
    m[coords[0]][coords[1]] = 1
    return False

def posa_arena_2(m):
    coords = [0, 500]
    block = False

    while not block:
        if m[1][499] == 1 and m[1][500] == 1 and m[1][501] == 1:
            return True
        if mat[coords[0]+1, coords[1]] == 0:
            coords[0] += 1
        elif mat[coords[0]+1, coords[1]-1] == 0:
            coords[0] += 1
            coords[1] -= 1
        elif mat[coords[0]+1, coords[1]+1] == 0:
            coords[0] += 1
            coords[1] += 1
        else: block = True
    m[coords[0]][coords[1]] = 1
    return False

mat = np.zeros((1000, 1000), dtype = 'int')
max_y = 0
for l in lines:
    parelles = l.split("->")
    for i in range(len(parelles)-1):
        x1, y1 = parelles[i].split(",")
        x2, y2 = parelles[i+1].split(",")
        max_y = max(max_y, int(y1), int(y2))
        posa_terra(int(x1), int(y1), int(x2), int(y2), mat)


posa_terra(0, max_y+2, 999, max_y+2, mat)

mat = mat.T


print(mat[0:13, 490:520,])



fi = False
c = 0
while not fi:
    fi = posa_arena_2(mat)
    #if not fi: c += 1 #part 1
    c += 1
print(mat[0:13, 490:520,])
print("Arena acumulada", c)

