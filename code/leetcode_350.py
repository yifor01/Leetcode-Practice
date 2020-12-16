# 350. Intersection of Two Arrays II
'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

# Solution 1 by Yifor
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) != len(nums2):
            min_set = [nums1, nums2][int(len(nums1) > len(nums2))]
            max_set = [nums1, nums2][int(len(nums1) < len(nums2))]
        else:
            min_set, max_set = nums1, nums2
        output_set = []

        for i in min_set:
            try:
                pos = max_set.index(i)
                output_set.append(i)
                max_set[pos] = None
            except:
                pass
        return output_set
'''time complexity: O(n**2) , space complexity: O(n)'''

# Solution 2 by Yifor
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        inter_set = list(set(nums1)&set(nums2))
        output = []
        for i in inter_set:
            reptimes = min(nums1[i],nums2[i])
            output.extend([i]*reptimes)
        return output
'''time complexity: O(n) , space complexity: O(n)'''
