# 268. Missing Number
'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
'''

# Solution 1 by Yifor
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = dict(zip(nums,nums))
        for i in range(len(nums)+1):
            if i not in nums:
                return i
'''time complexity: O(n) , space complexity: O(n)'''

# Solution 2 by Yifor
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
'''time complexity: O(n**2) , space complexity: O(1)'''