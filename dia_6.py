entrada = open("input_6")
lines = entrada.readlines()
entrada.close()

def tots_diferents(item):
    return len(set(item)) == len(item)

l = lines[0]
#l = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

i = 13
while i < len(l) and not tots_diferents(l[i-13:i+1]):
    i += 1

print(i+1)
