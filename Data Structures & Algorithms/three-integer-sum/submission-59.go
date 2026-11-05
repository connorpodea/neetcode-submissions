func threeSum(nums []int) [][]int {
    res := [][]int{}
    sort.Ints(nums)    
    
    for i := 0; i < len(nums) - 2; i += 1 {
        if i > 0 && nums[i] == nums[i - 1] {
            continue
        }

        l := i + 1
        r := len(nums) - 1

        for l < r {
            sum := nums[i] + nums[l] + nums[r]

            if sum == 0 {
                res = append(res, []int{nums[i], nums[l], nums[r]})
                l += 1
                r -= 1
                
                for l < r && nums[l] == nums[l - 1] {
                    l += 1
                }
                for r > l && nums[r] == nums[r + 1] {
                    r -= 1
                }
            }else if sum < 0 {
                l += 1
            }else {
                r -= 1
            }
        }
    }
    return res
}
