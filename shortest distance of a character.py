import re

S = "loveleetcode"
C = 'e'

list_words = []
list_index = []

if C in S:
    list_words = S.split(C)
    
#output[position_C] = 0
#print(position_C)
print(list_words)

array_each_word = []
for each_word in list_words:
    print(each_word)
    l = len(each_word)
    print(l)
    if each_word == '':
        array_each_word.append(0)
    #l = 0
    for each_char in each_word:
        array_each_word.append(l)
        print(each_char,'\t',l)
        l = l-1
    print(array_each_word)

'''S_reverse = (S[::-1])
output = {}
print(S_reverse)

if C in S:
    position_C = S_reverse.index(C)
    #print(position_C)
    list_words = S.strip(C)
    output[position_C] = 0
#print(position_C)
#print(list_words)

i=0
for each in list_words[::-1]:
    if each != C:
        output[list_words[::-1].index(each)] = i+1

print(output)'''


'''
-----------
num = ['0','1','3','4','5','6','7','8','9']
if C not in S:
    print("didnt find", C, "in string",S)
else:
    for i in S:
        if i in num:
            continue
        else:
            list_words = S.strip(C)
            if C not in list_words:
                break
            else:
                for j in list_words:
                    if j in num:
                        continue
                    else:
                        list_words.replace(list_words,list_words.strip(C))
print(list_words)'''
            
'''for each in re.finditer(C,S):
    print(C,' found', each.start(), each.end())
print (S.replace(C, "0"))'''
    
'''for each_c in S:
    if (each_c == C):
        list_index.append(S.index(each_c))
print(list_index)'''
        



