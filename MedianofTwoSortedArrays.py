import math

nums1 = [1,2]
nums2 = [3,4]

nums = nums1+nums2
nums.sort()
print(nums)

if (len(nums)%2) != 0:
    n = nums[math.floor(len(nums)/2)]
    print(n/1.0)
else:
    print(len(nums))
    l = len(nums)//2
    print(l)
    print((nums[l] + nums[l-1])/2)
