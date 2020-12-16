# 349. Intersection of Two Arrays (Easy)
'''
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:
Each element in the result must be unique.
The result can be in any order.
'''

# Solution by Yifor
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res,numdict = [],{}
        for num in nums1:
            numdict[num]=1
        for num in nums2:
            if num in numdict and numdict[num]:
                res.append(num)
                numdict[num]-=1
        return res

'''time complexity: O(n) , space complexity: O(n)'''