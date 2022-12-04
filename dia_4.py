entrada = open("input_4")
lines = entrada.readlines()
entrada.close()

c = 0
for l in lines:
    p1, p2 = l.split(",")
    n1, n2 = p1.split("-")
    n1, n2 = int(n1), int(n2)
    m1, m2 = p2.split("-")
    m1, m2 = int(m1), int(m2)

    """
    if(n1 <= m1 and n2 >= m2):
        c+=1
    elif(n1 >= m1 and n2 <= m2):
        c+=1
        """

    if (n1 <= m1 <= n2 or n1 <= m2 <= n2 or m1 <= n1 <= m2 or m1 <= n2 <= m2):
        c += 1
print(c)
