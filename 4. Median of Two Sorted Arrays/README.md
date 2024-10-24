# Median of Two Sorted Arrays

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

### Example 1:

<div style="border-left: 2px solid #555; padding-left: 10px;">

**Input:** nums1 = [1,3], nums2 = [2] <br>
**Output:** 2.00000<br>
**Explanation:** merged array = [1,2,3] and median is 2.

</div>

### Example 2:

<div style="border-left: 2px solid #555; padding-left: 10px;">

**Input:** nums1 = [1,2], nums2 = [3,4] <br>
**Output:** 2.50000 <br>
**Explanation:** merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

</div>

### Constraints:

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10⁶ <= nums1[i], nums2[i] <= 10⁶`
