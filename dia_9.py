entrada = open("input_91")
lines = entrada.readlines()
entrada.close()

def move(direction, coords):
    if direction == "R":
        coords[1] += 1
    elif direction == "L":
        coords[1] -= 1
    elif direction == "D":
        coords[0] -= 1
    else:
        coords[0] += 1

def move_tail(head, tail):
    t0 = 0
    t1 = 0
    if abs(head[1] - tail[1]) > 1 or (abs(head[1] - tail[1]) == 1 and abs(head[0] - tail[0]) > 1):
        if head[1] > tail[1]:
            t1 = 1
        else:
            t1 = -1
    if abs(head[0] - tail[0]) > 1 or (abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) > 1):
        if head[0] > tail[0]:
            t0 = 1
        else:
            t0 = -1
    tail[0] += t0
    tail[1] += t1


tail_pos = set()


head = [0,0]
tail = [0,0]
for l in lines:
    m, n = l.split()
    n = int(n)
    #print(m, n)
    for i in range(n):
        move(m, head)
        #print(head)
        move_tail(head, tail)
        #print(tail)
        tail_pos.add(tuple(tail))

print("Primer",len(tail_pos))

tail_pos = set()
knots = [[0,0] for i in range(10)]
for l in lines:
    m, n = l.split()
    n = int(n)
    #print(m, n)
    for i in range(n):
        move(m, knots[0])
        #print("H",knots[0])
        for j in range(1,10):
            move_tail(knots[j-1], knots[j])
            #if knots[j] != [0,0]:
                #print(j, knots[j])
        tail_pos.add(tuple(knots[9]))

print("Segon",len(tail_pos))
