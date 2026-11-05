func searchMatrix(matrix [][]int, target int) bool {
    l, r := 0, len(matrix) * len(matrix[0]) - 1

    for l <= r {
        m := (l + r) / 2
        cols := len(matrix[0])
        row := m / cols
        col := m % cols

        switch {
            case matrix[row][col] < target:
                l = m + 1
            case matrix[row][col] > target:
                r = m - 1
            case matrix[row][col] == target:
                return true
        }
    }
    return false
}
