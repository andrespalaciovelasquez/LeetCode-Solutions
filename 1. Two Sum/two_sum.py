# Time complexity: O(n) - Linear time complexity

def twoSum(nums, target):
    num_dict = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], index]
        num_dict[num] = index

    return []

# Example usage:
nums1 = [2, 7, 11, 15]
target1 = 9
result1 = twoSum(nums1, target1)
print(result1)  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
result2 = twoSum(nums2, target2)
print(result2)  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
result3 = twoSum(nums3, target3)
print(result3)  # Output: [0, 1]
