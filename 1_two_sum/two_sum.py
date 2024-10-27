from typing import List


# Time complexity: O(n) - Linear time complexity
def two_sum(nums: List[int], target: int) -> List[int]:
    num_dict = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in num_dict:
            return [num_dict[complement], index]

        num_dict[num] = index

    return []


# Example 1:
nums1 = [2, 7, 11, 15]
target1 = 9
result1 = two_sum(nums1, target1)
print(result1)  # Output: [0, 1]

# Example 2:
nums2 = [3, 2, 4]
target2 = 6
result2 = two_sum(nums2, target2)
print(result2)  # Output: [1, 2]

# Example 3:
nums3 = [3, 3]
target3 = 6
result3 = two_sum(nums3, target3)
print(result3)  # Output: [0, 1]
