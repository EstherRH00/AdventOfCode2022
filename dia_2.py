entrada = open("input_2")
lines = entrada.readlines()
entrada.close()

# rock: +1, paper +2, scissors +3
# A = X = rock, B = Y = paper, C = Z = scissors
# rock 0 < paper 1 < scissors 2 < rock 3
score = 0

"""PART 1
scores = {"X": 1, "Y": 2, "Z": 3}

def AtoX(x): return chr(ord(x)+23) # A-> X B->Y C->Z

for parella in lines:
    x, y = parella.split()
    score += scores[y]
    x = AtoX(x)
    if x == y:
        score += 3
    elif (x == "X" and y == "Y") or (x == "Y" and y == "Z") or (x == "Z" and y == "X"):
        score += 6
print(score)
"""

#PART 2
scores = {"X": 1, "Y": 2, "Z": 3}

def AtoX(x): return chr(ord(x)+23) # A-> X B->Y C->Z

for parella in lines:
    x, y = parella.split()
    x = AtoX(x)
    z = None
    if y == "X": #perdre
        z = chr(ord(x)-1) if x != "X" else "Z"
    elif y == "Y": #empat
        z = x
        score += 3
    else: #guanyar
        z = chr(ord(x) + 1) if x != "Z" else "X"
        score += 6
    score += scores[z]
print(score)
