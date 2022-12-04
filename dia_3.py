entrada = open("input_3")
lines = entrada.readlines()
entrada.close()

def letterToValue(x): return ord(x)-ord("a") + 1 if x.islower() else ord(x)-ord("A") + 27

def trobaComu(l1, l2):
    for i in l1:
        if i in l2:
            return i

def trobaComu2(l1, l2, l3):
    for i in l1:
        if i in l2 and i in l3:
            return i
acc = 0
"""
for l in lines:
    m1 = l[:len(l)//2]
    m2 = l[len(l) // 2:]
    acc+= letterToValue(trobaComu(m1, m2))

print(acc)
"""

for i in range(0,len(lines),3):

    acc+= letterToValue(trobaComu2(lines[i], lines[i+1], lines[i+2]))

print(acc)