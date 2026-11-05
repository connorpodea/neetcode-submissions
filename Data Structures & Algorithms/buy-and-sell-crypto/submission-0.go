func maxProfit(prices []int) int {
	minPrice := prices[0]
	best := 0

	for _, p := range prices {
		best = max(best, p - minPrice)
		minPrice = min(minPrice, p)
	}
	return best
}
