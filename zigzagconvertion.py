s = "paypalishiring"
rows = 3
sec_row = rows-2
print("length of string",len(s))

l = []
z = ""
fr = 0
for i in range(len(s)):
    if i == 0:
        z = s[i]
    else:
        for i in range(0,rows):
            if i == (fr + rows + sec_row):
                fr = fr+rows+sec_row
                print(fr)
                z = z+s[fr]
l.append(z)
print(z)
print(l)

z = ""
sr = 0
for i in range(len(s)):
    if i == 1:
        z = s[i]
    elif i == (sr+rows):
        sr = sr+sec_row
        z = z+s[sr]
print(z)