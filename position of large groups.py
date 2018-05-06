S = "aaa"
listindex = []
listall = []
index = 0
for each_ch in S:
    if index == 0:
        listindex.append(index)
        pre_index = index
        index = index+1
        pre_char = each_ch
    elif pre_char == each_ch:
        pre_index = index
        pre_char = each_ch
        index = index + 1
    else:
        listindex.append(pre_index)
       # print(listindex)
        if listindex[1] - listindex[0] >= 2:
            listall.append(listindex[:])
        del listindex[:]
        listindex.append(index)
        pre_char = each_ch
        pre_index = index
        index = index + 1
    
listindex.append(pre_index)
#print(listindex)
if listindex[1] - listindex[0] >= 2:
    listall.append(listindex[:])
print(listall)