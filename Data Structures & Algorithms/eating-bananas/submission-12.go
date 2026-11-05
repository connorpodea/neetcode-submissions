func minEatingSpeed(piles []int, h int) int {
    min, max := 1, 0
    for _, n := range piles {
        if n > max {
            max = n
        }
    }

    k := max

    for min <= max {
        speed := (min + max) / 2
        time := 0

        for _, n := range piles {
            time += (n + speed - 1) / speed
        }

        if time <= h{
            k = speed
            max = speed - 1
        } else {
            min = speed + 1
        }
    }
    return k
}