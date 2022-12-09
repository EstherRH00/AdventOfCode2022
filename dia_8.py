import numpy as np

entrada = open("input_8")
lines = entrada.readlines()
entrada.close()

def is_visible(i,j,matriu):
    visible = np.asarray([True, True, True, True]) #si no en trobo cap pels quatre cantons
    #per fila
    jj = 0 #busco un arbre mes alt
    while jj < j and visible[0]:
        if matriu[i][jj] >= matriu[i][j]:
            visible[0] = False
        jj += 1

    jj = len(matriu[0])-1  # busco un arbre mes alt
    while jj > j and visible[1] and not visible[0]:
        if matriu[i][jj] >= matriu[i][j]:
            visible[1] = False
        jj -= 1

    # per columna
    ii = 0  # busco un arbre mes alt
    while ii < i and visible[2] and not visible[1] and not visible[0]:
        if matriu[ii][j] >= matriu[i][j]:
            visible[2] = False
        ii += 1

    ii = len(matriu) - 1  # busco un arbre mes alt
    while ii > i and visible[3] and not visible[2] and not visible[1] and not visible[0]:
        if matriu[ii][j] >= matriu[i][j]:
            visible[3] = False
        ii -= 1

    return np.any(visible)

def scenic_score(i,j,matriu):
    sc = 1
    block = False
    jj = j-1  # busco un arbre mes alt
    v = 0
    while 0 <= jj < j and not block:
        if matriu[i][jj] >= matriu[i][j]:
            block = True
        jj -= 1
        v += 1
    sc *= v
    v= 0
    block = False
    jj = j + 1 # busco un arbre mes alt
    while len(matriu[0]) > jj > j and not block:
        if matriu[i][jj] >= matriu[i][j]:
            block = True
        jj += 1
        v += 1
    sc *= v

    block = False
    ii = i - 1  # busco un arbre mes alt
    v = 0
    while 0 <= ii < i and not block:
        if matriu[ii][j] >= matriu[i][j]:
            block = True
        ii -= 1
        v += 1
    sc *= v
    v = 0
    block = False
    ii = i + 1  # busco un arbre mes alt
    while len(matriu) > ii > i and not block:
        if matriu[ii][j] >= matriu[i][j]:
            block = True
        ii += 1
        v += 1
    sc *= v
    return sc

mat = np.zeros((len(lines), len(lines[0])-1), dtype='int')

for i in range(len(lines)):
    for j in range(len(lines[i])-1):
        mat[i][j] = int(lines[i][j])
print(mat)

r,c = mat.shape
vs = 2*(r-1)+2*(c-1)
print(r,c,vs)
for i in range(1, r-1):
    for j in range(1, c-1):
        if is_visible(i, j, mat):
            vs += 1

print("visible", vs)

vision_score = 0
for i in range(1, r-1):
    for j in range(1, c-1):
        tmp = scenic_score(i, j, mat)
        if tmp > vision_score:
            vision_score = tmp
print("Scenic score", vision_score)