s = "pwwkew"

'''if s == "":
    print(0)
dic = []
for i in range(0,len(s)+1):
    for j in range(1,len(s)+1):
        if (s[i:j] not in dic):
            if len(s[i:j]) == len(set(s[i:j])):
                dic.append(s[i:j])
dic.sort(key=len, reverse=True)
print(len(dic[0]))'''

l = len(s)
print("Length:",l)
dic = []
for i in range(0,len(s)+1):
    #for j in range(1,l+1):
    j = len(s)+1
    while j:
        if (s[i:j] not in dic): # 0:7 | 0:6, 1:7| 0:5, 1:6, 2:7 | 0:4, 1:5, 2:6, 3:7 |
            dic.append(s[i:j])
        j = j-1
print(dic)
dic.sort(key=len, reverse=True)
print(dic)

for each in dic:
    #print(len(each))
    #print(len(set(each)))
    if len(each) == len(set(each)):
        print(each,len(each))
        break