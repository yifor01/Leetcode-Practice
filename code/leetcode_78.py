# 78. Subsets
'''
Question:
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

# Solution by Yifor
class Solution:
    def __init__(self):
        self.output = []
    def subsets(self,nums,path=[]):
        self.output.append(path)
        for i in range(len(nums)):
             self.subsets(nums[i+1:] , path+[nums[i]] )
        return self.output
        
'''time complexity: O(n*2^n) , space complexity: O(2^n)'''