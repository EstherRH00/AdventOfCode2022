entrada = open("input")
lines = entrada.readlines()
entrada.close()

nombres = []

for l in lines:
    if l != "\n":
        nombres.append(int(l))
        if(int(l) == 0):
            print("Error", l)
    else:
        nombres.append(0)
nombres.append(0)

print(nombres)

maxim_1 = 0
maxim_2 = 0
maxim_3 = 0
max_temp = 0

for n in nombres:
    if n != 0:
        max_temp += n
    else:
        if maxim_1 < max_temp:
            maxim_3 = maxim_2
            maxim_2 = maxim_1
            maxim_1 = max_temp
        elif maxim_2 < max_temp:
            maxim_3 = maxim_2
            maxim_2 =  max_temp
        elif maxim_3 < max_temp:
            maxim_3 = max_temp
        max_temp = 0
print(maxim_1 + maxim_2 + maxim_3)
