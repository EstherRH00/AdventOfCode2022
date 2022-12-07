class Tree:
    def __init__(self, data, parent = None):
        self.parent = parent
        self.children = []
        self.data = data
        self.suma = 0


    def PrintTree(self):
        if self.suma != 0:
            print(self.data, "s:", self.suma, end = " - "),
        else:
            print(self.data, end = " - "),
        if self.children != []:
            for c in self.children:
                c.PrintTree()

    def atMost100(self):
        sTmp = 0
        if self.suma <= 100000 and self.children != []:
            # si es directori sumo
            sTmp += self.suma
        for c in self.children:
            sTmp += c.atMost100()
        return sTmp

    def toDelete(self, toFree):
        sTmp = float('inf')
        if self.suma >= toFree and self.children != []:
            # si es directori sumo
            sTmp = self.suma
            sumes = [sTmp]
            for c in self.children:
                sumes.append(c.toDelete(toFree))
            sTmp = min(sumes)
        return sTmp

entrada = open("input_7")
lines = entrada.readlines()
entrada.close()

root= Tree("root")
actual = root
for l in lines:
    parts = l.split()
    if parts[0] == "$" and parts[1] == "cd":
        if parts[2] == "/":
            actual = root
        elif parts[2] == "..":
            if actual.parent != None:
                actual = actual.parent
        else:
            for c in actual.children:
                if c.data == parts[2]: actual = c

    elif parts[0].isdigit():
        actual.children.append(Tree(parts[0], parent = actual))

        s = int(parts[0])
        n = actual
        while n != None:
            n.suma += s
            n = n.parent
    elif parts[0] =="dir":
        actual.children.append(Tree(parts[1], parent = actual))

print("\nSuma", root.atMost100())

unused = 70000000 - root.suma
toFree = 30000000 - unused

print("Delete", root.toDelete(toFree))


