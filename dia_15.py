import numpy as np

entrada = open("input_15")
lines = entrada.readlines()
entrada.close()

def pinta_sensor(mat, x, y, r): #x es columna, y es fila
    #print("pintant a ", x, y, "amb radi", r)
    for i in range(-r, r+1):
        #print("esquerra:", x + r - abs(i), "dreta", x - r + abs(i))
        start = min(- r + abs(i), + r - abs(i))
        stop = max(- r + abs(i), + r - abs(i))

        #print("Start:", - r + abs(i), "stop", + r - abs(i))

        for j in range(start, stop+1):
            if x+j < 4000000 and y + i < 4000000:
                mat[x+j][y+i]=2
    #print(mat[x-2*r:x+2*r, y-2*r:y+2*r])

def distancia_horitzontal_vertical(a,b,x,y):
    return abs(x-a), abs(y-b)

def distancia_manhattan(a,b,x,y):
    return abs(x-a) + abs(y-b)

def conta_obstacles(obstacles, origen, salt):
    #print("obstacles", obstacles, "origen", origen, "salt", salt)
    o = [1 for i in obstacles if (i - origen) < salt and (i - origen) > 0]
    #print("retorno",o,len(o))
    return len(o)

m = []

for l in lines:
    l = l.replace(",", " ")
    l = l.replace(":", " ")
    parts = l.split()

    #Sensor at x=2, y=18: closest beacon is at x=-2, y=15
    x = int(parts[2].split("=")[1])
    y = int(parts[3].split("=")[1])
    z = int(parts[8].split("=")[1])
    t = int(parts[9].split("=")[1])
    r = distancia_manhattan(x,y,z,t)
    m.append([x,y,z,t,r])

m = sorted(m, key=lambda x: x[4])

m = np.asarray(m)

#print(m)
min_x = min(min(m[:,0]), min(m[:,2]))
max_x = max(max(m[:,0]), max(m[:,2]))
min_y = min(min(m[:,1]), min(m[:,3]))
max_y = max(max(m[:,1]), max(m[:,3]))
rmax = max(m[:,4])

#print(min_x, max_x, min_y, max_y, rmax)


#board = np.zeros((max_y+1-min_y+2*rmax, max_x+1-min_x+2*rmax), dtype = int) #padding de rmax per tots els costats
                                                                            #y son files, x columnes
#print(board.shape)
sensors_radis = {} #key: parelles x, y, value radi
#print(m)
obstacles = set()
fila = 2000000-min_y+rmax
for x,y,z,t,r in m:
    x = x-min_x+rmax
    y = y - min_y+rmax
    z = z -min_x+rmax
    t = t - min_y+rmax
    #print(x,y,z,t)
    if fila == y:
        obstacles.add(x)
    if fila == t:
        obstacles.add(z)
    if (x, y) not in sensors_radis.keys():
        sensors_radis[(x, y)] = r
obstacles = list(obstacles)
#print(sensors_radis)

cont = 0
i = 0
obstacles.sort()

#PART 1
"""
#print("Obstacles", obstacles)
print("He d'arribar a ", max_x+1-min_x+2*rmax)
while i < max_x+1-min_x+2*rmax:

    #print("posicio", i)
    salt = 0
    afectat = False
    for s, r in sensors_radis.items():
        hor = s[0] - i
        if distancia_manhattan(i, fila, s[0], s[1]) <= r and hor > 0:
            afectat = True
            #print("Soc a", i, fila, "M'afecta el sensor", s,"disrancia",distancia_manhattan(i, fila, s[0], s[1]), "amb radi", hor)
            salt_temp = hor + 1 + (r - abs(fila-s[1])) #per si no es simetric
            salt = max(salt, salt_temp)

    if afectat:
        cont += salt
        cont -= conta_obstacles(obstacles, i, salt)
    i += max(salt,1)


print("apartat 1:",cont)

"""
def afectat(fila):
    i = rmax-min_x
    while i < rmax+4000000:
        # print("posicio", i)
        salt = 0
        a = False
        for s, r in sensors_radis.items():
            hor = s[0] - i
            if distancia_manhattan(i, fila, s[0], s[1]) <= r:
                a = True
                if hor > 0:
                    # print("Soc a", i, fila, "M'afecta el sensor", s,"disrancia",distancia_manhattan(i, fila, s[0], s[1]), "amb radi", hor)
                    salt_temp = hor + 1 + (r - abs(fila - s[1]))  # per si no es simetric
                    salt = max(salt, salt_temp)
        if not a:
            return i
        i += max(salt, 1)
    return None

for j in range(rmax - min_y, rmax + 4000000 +1): # files
    if j % 1000000 == 0:
        print(j)
    a = afectat(j)
    if a != None:
        print("NO AFECTAT")
        print(a-rmax+min_x, j-rmax+min_y)
        print("RESULTAT",4000000  * (a-rmax+min_x) + j-rmax+min_y)

