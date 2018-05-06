haystack = "mississippi"
needle = "pi"

haystack = haystack.strip()
needle = needle.strip()

l=len(needle)
pos = 0
dic = {}
for i in range(len(haystack)):
    print(i)
    if (len(haystack[i:l]) == len(needle)):
        if (haystack[i:l] not in dic):
            dic[haystack[i:l]]=pos
            print(dic)
        pos += 1
        l=l+1
    else:
        break
print(dic)
if needle in dic:
    print(dic[needle])
elif haystack == "" and needle == "":
    print(0)
else:
    print(-1)
