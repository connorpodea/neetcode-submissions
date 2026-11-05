import (
    "cmp"
    "slices"
)

func carFleet(target int, position []int, speed []int) int {
	n := len(position)
	if n == 0 {
		return 0
	}

	type car struct {
		position int
		speed    int
	}

	// 1. Group positions and speeds
	cars := make([]car, n)
	for i := 0; i < n; i++ {
		cars[i] = car{position: position[i], speed: speed[i]}
	}

	// 2. Sort by position in ascending order (furthest to closest)
	slices.SortFunc(cars, func(a, b car) int {
		return cmp.Compare(a.position, b.position)
	})

	// 3. Compute completion times using the SORTED cars slice
	completionTimes := make([]float64, n)
	for i := 0; i < n; i++ {
		// Cast to float64 BEFORE division to preserve precision
		completionTimes[i] = float64(target-cars[i].position) / float64(cars[i].speed)
	}

	// 4. Process from closest to target (end of slice) backwards
	res := 1
	currentFleetTime := completionTimes[n-1]

	for i := n - 2; i >= 0; i-- {
		if completionTimes[i] > currentFleetTime {
			res++
			currentFleetTime = completionTimes[i]
		}
	}

	return res
}