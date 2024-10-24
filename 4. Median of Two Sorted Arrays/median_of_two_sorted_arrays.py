# Time complexity: O(log(min(m, n)))

def medianOfTwoSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total_len = m + n
    half = total_len // 2

    left, right = 0, m

    while left <= right:
        partition1 = (left + right) // 2
        partition2 = half - partition1

        # Edge cases for partitions (handling out of bounds)
        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]

        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]

        # Check if we found the correct partition
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # If the total length is odd, return the middle element
            if total_len % 2 == 1:
                return min(minRight1, minRight2)
            # If the total length is even, return the average of the two middle elements
            return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2

        # Adjust the partition1 boundaries
        elif maxLeft1 > minRight2:
            right = partition1 - 1
        else:
            left = partition1 + 1

# Example usage
nums1 = [1, 3, 8]
nums2 = [7, 9, 10, 11]

median = medianOfTwoSortedArrays(nums1, nums2)
print(f"The median is: {median}") # Output: 8