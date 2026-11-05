func searchMatrix(matrix [][]int, target int) bool {
    l, r := 0, len(matrix) * len(matrix[0]) - 1

    for l <= r {
        m := (l + r) / 2
        row := m / len(matrix[0])
        col := m % len(matrix[0])
        cur := matrix[row][col]

        switch {
            case cur < target:
                l = m + 1
            case cur > target:
                r = m - 1
            case cur == target:
                return true
        }
    }
    return false
}
