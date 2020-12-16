# 46. Permutations
'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

# Solution by Yifor
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [ [nums[x]] + p for x in range(len(nums)) for p in self.permute(nums[:x]+nums[x+1:])  ] or [[]]

'''time complexity: O(n!) , space complexity: O(1)'''