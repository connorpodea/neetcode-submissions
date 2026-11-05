from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # The O(log(m + n)) is way too difficult to comprehend, just gonna do the intuitive version.
        total_len = len(nums1) + len(nums2)
        index1, index2 = 0, 0
        merged = []

        # Step through both arrays and append the smaller value
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] < nums2[index2]:
                merged.append(nums1[index1])
                index1 += 1
            else:
                merged.append(nums2[index2])
                index2 += 1

        # If there are leftovers in nums1, dump them in
        while index1 < len(nums1):
            merged.append(nums1[index1])
            index1 += 1

        # If there are leftovers in nums2, dump them in
        while index2 < len(nums2):
            merged.append(nums2[index2])
            index2 += 1

        # Find the median from the merged list
        mid = total_len // 2
        if total_len % 2 == 1:
            # Odd total length: return the exact middle element
            return float(merged[mid])
        else:
            # Even total length: average the two middle elements
            return (merged[mid - 1] + merged[mid]) / 2.0