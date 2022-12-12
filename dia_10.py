entrada = open("input_10")
lines = entrada.readlines()
entrada.close()


def display(mat):
    for f in mat:
        for c in f:
            print(c, end="")
        print()

x = 1
sum_intensities = 0
cicle = 0

for l in lines:
    #print(l)
    if l == "noop\n" or l == "noop":
        cicle += 1
        if cicle % 40 == 20 and  cicle <221:
            sum_intensities += x*cicle
            print(cicle, x, sum_intensities)
    else:
        m,n = l.split()
        cicle += 1
        if cicle % 40 == 20 and cicle <221:
            sum_intensities += x*cicle
            print(cicle, x, sum_intensities)
        cicle += 1
        if cicle % 40 == 20 and cicle <221:
            sum_intensities += x*cicle
            print(cicle, x, sum_intensities)
        x += int(n)

print(sum_intensities)


x = 1
sum_intensities = 0
cicle = 0
mat =[[0 for i in range(40)]for j in range(6)]
for l in lines:
    if(cicle < 241):
        print("cicl2",cicle,cicle//40,cicle%40)
        if l == "noop\n" or l == "noop":
            mat[cicle//40][cicle%40] = "#" if (x-1) <= cicle%40 <= (x+1) else "."
            cicle += 1
        else:
            m,n = l.split()
            mat[cicle // 40][cicle % 40] = "#" if (x-1) <= cicle%40 <= (x+1)  else "."
            cicle += 1
            if(cicle < 241):
                mat[cicle // 40][cicle % 40] = "#" if (x-1) <= cicle%40 <= (x+1)  else "."
                cicle += 1
                x += int(n)

print("x",x, "cicle",cicle)
display(mat)