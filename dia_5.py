entrada = open("input_5")
lines = entrada.readlines()
entrada.close()

#l = [1,2,3]
#a = l.pop()
#print(a, l) #3, [1,2]
#l.append(4)
#print(l) #[1,2,4]

def display(m):
    for f in m: print(f)

mat = [[] for i in range(9)]#3
for l in lines[:8]:#3
    for i in range(1, len(l), 4):
        if l[i] != " ":
            mat[(i-1)//4].insert(0, l[i])

display(mat)
"""
for l in lines[10:]:#5
    inst = l.split()
    for i in range(int(inst[1])):
        a = mat[int(inst[3])-1].pop()
        mat[int(inst[5])-1].append(a)
"""

for l in lines[10:]:#5
    inst = l.split()
    mov = mat[int(inst[3])-1][-int(inst[1]):]
    remain = mat[int(inst[3])-1][:-int(inst[1])]
    mat[int(inst[3])-1] = remain
    mat[int(inst[5])-1] += mov

for l in mat:
    print(l.pop(), end = "")
