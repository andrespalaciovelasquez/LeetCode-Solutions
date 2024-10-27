from typing import List, Union


# Time complexity: O(log(min(m, n)))
def median_of_two_sorted_arrays(
    nums1: List[Union[int, float]], nums2: List[Union[int, float]]
) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total_len = m + n
    half = total_len // 2

    left, right = 0, m

    while left <= right:
        partition1 = (left + right) // 2
        partition2 = half - partition1

        max_left1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float("inf") if partition1 == m else nums1[partition1]

        max_left2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float("inf") if partition2 == n else nums2[partition2]

        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if total_len % 2 == 1:
                return min(min_right1, min_right2)
            return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2

        elif max_left1 > min_right2:
            right = partition1 - 1
        else:
            left = partition1 + 1


# Example 1:
nums1 = [1, 3]
nums2 = [2]
median = median_of_two_sorted_arrays(nums1, nums2)
print(f"The median is: {median}")  # Output: 2

# Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
median = median_of_two_sorted_arrays(nums1, nums2)
print(f"The median is: {median}")  # Output: 2.5

# Example 3:
nums1 = [1, 3, 8]
nums2 = [7, 9, 10, 11]
median = median_of_two_sorted_arrays(nums1, nums2)
print(f"The median is: {median}")  # Output: 8
