#monkeys = [[79, 98], [54, 65, 75, 74], [79, 60, 97], [ 74]]
#sniffed = [0,0,0,0]
monkeys = [[77, 69, 76, 77, 50, 58],[75, 70, 82, 83, 96, 64, 62], [ 53], [85, 64, 93, 64, 99], [61, 92, 71], [79, 73, 50, 90], [50, 89], [83, 56, 64, 58, 93, 91, 56, 65]]
sniffed = [0 for i in range(8)]

acc = 5 *17*2*7*3*11*13*19

for i in range(10000):
    for j in range(len(monkeys)):
        while monkeys[j]:
            a = monkeys[j].pop()
            sniffed [j] +=1
            if j == 0:
                a = (a*11) % acc
                if a%5 == 0:
                    monkeys[1].append(a)
                else:
                    monkeys[5].append(a)
            elif j == 1:
                a = (a+8)% acc
                if a%17 == 0:
                    monkeys[5].append(a)
                else:
                    monkeys[6].append(a)
            elif j == 2:
                a = (a*3)% acc
                if a%2 == 0:
                    monkeys[0].append(a)
                else:
                    monkeys[7].append(a)
            elif j == 3:
                a = (a+4)% acc
                if a%7 == 0:
                    monkeys[7].append(a)
                else:
                    monkeys[2].append(a)
            elif j == 4:
                a = (a**2)% acc
                if a%3 == 0:
                    monkeys[2].append(a)
                else:
                    monkeys[3].append(a)
            elif j == 5:
                a = (a+2)% acc
                if a%11 == 0:
                    monkeys[4].append(a)
                else:
                    monkeys[6].append(a)
            elif j == 6:
                a = (a+3)% acc
                if a%13== 0:
                    monkeys[4].append(a)
                else:
                    monkeys[3].append(a)
            else:
                a = (a + 5)% acc
                if a % 19 == 0:
                    monkeys[1].append(a)
                else:
                    monkeys[0].append(a)
print(monkeys)
print(sniffed)
sniffed.sort()

print(sniffed[7]*sniffed[6])

