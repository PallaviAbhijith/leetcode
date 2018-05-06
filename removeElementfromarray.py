nums = [3,2,3]
val = 3
#nums = [i for i in nums if i != val ]
#print(nums)
st = "Hello"
s = "llo"
print(len(st))
print(len(s))
print(len(st)-len(s)+1)
print(st[2:6])

print(len(nums))
#l = len(nums)
'''for each in nums:
    print (each)
    print (nums)
    if each != val:
        nums = nums
    else:
        nums.remove(val)
        each = 0
       # print(len(nums))
print ('final list',nums)'''

while val in nums:
    nums.remove(val)
print ('final list',nums)