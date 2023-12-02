total = 0
first = 'c'
last = 'c'

with open("input.txt") as file:
    for line in file:
        idxs = [i for i in range(0, len(line)) if line[i].isdigit()]
        first = line[ idxs[0] ]
        last = line[ idxs[len(idxs)-1] ]
        total += int(str(first)+str(last) )
print(total)
