s = "cbbd"
#print(s[::-1])
pal = {}
for i in range(0,len(s)+1):
    for j in range(1,len(s)+1):
        st = s[i:j]
 #       print(st)
        if st == st[::-1]:
            pal[(st[::-1])] = len(st[::-1])

res = list(sorted(pal, key=pal.__getitem__, reverse=True))
print(res[0])