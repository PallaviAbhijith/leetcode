package twoSum

func twoSum(nums []int, target int) []int {
    i := 0
                    var s []int
    println(len(nums))
    for i < len(nums) {
        println(i)
        j := i + 1;
        for j < len(nums){
            println(j)
            if nums[i] + nums[j] == target {
                s[0] = i
                s[1]=j
                return s
//'                return (i,j)
            }
            j = j + 1
        }
        i = i + 1
    }
return s        
}