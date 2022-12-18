entrada = open("input_18")
lines = entrada.readlines()
entrada.close()

def es_de_la_comp(x,y,z, comp):
    for a,b,c in comp:
        if(es_toquen(a,b,c,x,y,z)):
            return True
    return False

def es_externa(comp, llista):
    # si es externa, qualsevol dels aires ha de tenir com a minim una direccio de sortida
    r = cares_externes(comp[0][0], comp[0][1], comp[0][2], llista)
    return r != 0

def es_toquen(a,b,c,x,y,z):
    if (a == x and y == b and abs(z-c) <= 1) or (a == x and z == c and abs(y-b) <= 1) or  (z == c and y == b and abs(x-a) <= 1):
        return True
    return False

def cares_externes(x,y,z,llista):
    # buscar si alguna, tirant una linia recta, arriba a l'infinit
    x_ext = [1, 1]
    y_ext = [1, 1]
    z_ext = [1, 1]
    i = 0
    while i < len(llista) and (1 == x_ext[0] or 1 == x_ext[1] or 1 == y_ext[0] or 1 == y_ext[1] or 1 == z_ext[0] or 1 == z_ext[1]):
        a ,b, c = llista[i]
        if (a == x and y == b and z - c > 0):
            z_ext[0] = 0
        if (a == x and y == b and z - c < 0):
            z_ext[1] = 0
        if (a == x and z == c and y - b > 0):
            y_ext[0] = 0
        if (a == x and z == c and y - b < 0):
            y_ext[1] = 0
        if (z == c and y == b and x - a > 0):
            x_ext[0] = 0
        if (z == c and y == b and x - a < 0):
            x_ext[1] = 0
        i += 1
    return sum(x_ext) + sum(y_ext) + sum(z_ext)

def get_veins(a,b,c):
    return [[a+1,b,c], [a-1,b,c], [a,b+1,c], [a,b-1,c], [a,b,c+1], [a,b,c-1]]

def get_veins_diag(a,b,c):
    return [[a+1,b,c], [a-1,b,c], [a,b+1,c], [a,b-1,c], [a,b,c+1], [a,b,c-1],
             [a+1,b+1,c], [a+1,b-1,c], [a-1,b+1,c],[a-1,b-1,c],
             [a,b+1,c+1], [a,b+1,c-1], [a,b-1,c+1],[a,b-1,c-1],
             [a+1,b,c+1], [a+1,b,c-1], [a-1,b,c+1],[a-1,b,c-1],
             [a+1, b + 1, c + 1], [a+1, b + 1, c - 1],
             [a - 1, b + 1, c + 1], [a - 1, b + 1, c - 1],
             [a + 1, b - 1, c + 1], [a + 1, b - 1, c - 1],
             [a - 1, b - 1, c + 1], [a - 1, b - 1, c - 1]]


def omple(comp, llista):
    print("Estic omplint", comp)
    c = comp
    veins = get_veins(comp[0][0], comp[0][1], comp[0][2])
    veins = [v for v in veins if v not in llista and v not in comp]
    i = 0
    while veins and i < 1000:
        print(veins)
        v = veins.pop()
        c.append(v)
        vv = [x for x in get_veins(v[0], v[1], v[2]) if x not in llista and x not in comp and x not in veins]
        veins += vv
        i+= 1
    return c

def cares(lines):
    # cares externes del conjunt llista
    llista = []
    cont = 0
    for x,y,z in lines:
        cont += 6
        for a, b, c in llista:
            if es_toquen(a, b, c, x, y, z):
                cont -= 2
        llista.append([x, y, z])
    print("cares", cont)
    return cont

llista = []
cont = 0
for l in lines:
    cont += 6
    ll = l.split(",")
    x = int(ll[0])
    y = int(ll[1])
    z = int(ll[2])
    for a,b,c in llista:
        if es_toquen(a,b,c,x,y,z):
            cont -= 2
    llista.append([x,y,z])

print("primera part", cont)
print(llista)

aire = []
comp_connexes_aire = []
for a,b,c in llista:
    veins = get_veins_diag(a,b,c)

    for x,y,z in veins:
        if [x,y,z] not in llista and [x,y,z] not in aire:
            aire.append([x, y, z])
            idx = []
            nova = [[x,y,z]]

            for i in range(len(comp_connexes_aire)):
                cmp = comp_connexes_aire[i]
                if es_de_la_comp(x,y,z,cmp):
                    nova += cmp
                    idx.append(i)

            for i in idx[::-1]:
                del comp_connexes_aire[i]

            comp_connexes_aire.append(nova)

print("hi ha", len(comp_connexes_aire), "components connexes")
print(comp_connexes_aire)
cont2 = 0
cc = 0
for comp in comp_connexes_aire:
    if not es_externa(comp, llista):
        print("no es externa", comp)
        c = omple(comp, llista)
        cont2 += cares(c)
        cc += len(c)
    else:
        print("la externaaaaaaaaaaa")

print("segona part", cont, cont2,  cont - cont2)
print(cc)