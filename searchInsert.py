inp = [1,3,5,6]
target = 0

if target not in inp:
    inp.append(target)
    inp.sort()
print(inp)
print(inp.index(target))