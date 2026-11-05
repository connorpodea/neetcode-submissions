func maxArea(heights []int) int {
    l, r := 0, len(heights) - 1
    res := 0

    for l < r {
        area := min(heights[l], heights[r]) * (r - l)

        if area > res {
            res = area
        }

        if heights[l] < heights[r] {
            l += 1
        } else {
            r -= 1
        }
    }
    return res
}

func min(n1, n2 int) int {
    if n1 < n2 {
        return n1
    }
    return n2
}