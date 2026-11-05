func isValidSudoku(board [][]byte) bool {
	rows := [9]int{}
	cols := [9]int{}
	boxes := [9]int{}

	for ri := 0; ri < 9; ri += 1 {
		for ci := 0; ci < 9; ci += 1 {
			b := board[ri][ci]
	
			if b == '.' {
				continue
			}

			boxNum := ((ri / 3) * 3) + (ci / 3)
			val := b - '0'
			bitMask := 1 << val

			if (rows[ri] & bitMask) != 0 || (cols[ci] & bitMask) != 0 || (boxes[boxNum] & bitMask) != 0 {
				return false
			}
			rows[ri] |= bitMask
			cols[ci] |= bitMask
			boxes[boxNum] |= bitMask
		}
	}
	return true
}
