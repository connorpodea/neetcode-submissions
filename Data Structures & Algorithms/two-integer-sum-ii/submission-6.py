class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            lnum = numbers[l]
            rnum = numbers[r]
            if lnum + rnum < target:
                l += 1
            elif lnum + rnum > target:
                r -= 1
            else:
                break

        return [l + 1, r + 1]