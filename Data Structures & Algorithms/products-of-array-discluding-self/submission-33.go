func productExceptSelf(nums []int) []int {
    res := make([]int, len(nums))
    prod := 1
    zeros := 0

    for _, n := range nums {
        if n == 0 {
            zeros += 1
            continue
        }
        prod *= n
    }

    if zeros > 1 {
        return res
    }

    for i := range nums {
        if zeros > 0 && nums[i] == 0 {
            res[i] = prod
        }
        if zeros == 0 {
            res[i] = prod / nums[i]
        }
    }
    return res
}
