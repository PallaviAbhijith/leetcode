list1 = [1, 1, 2, 3, 3, 3]
print(list1)
s = set(list1)
print(sorted(list(s)))

def removeDuplicates(nums):
    if not nums:
        return 0
    new_number = 0

    for i in range(1,len(nums)):
        print("i value=",i)
        if nums[i] != nums[new_number]:
            new_number += 1
            nums[new_number]=nums[i]
    return new_number + 1

print(removeDuplicates(list1))
