# 136. Single Number
'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

# Solution by Yifor

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        a = dict()
        for i in range(len(nums)):
            if nums[i] in  a:
                a[nums[i]]+=1
            else:
                a[nums[i]] = 1
        for i in a:
            if a[i] ==1:
                return i
                break
'''time complexity: O(n) , space complexity: O(n)'''

# Solution by Best Solution (XOR)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a^=i
        return a

'''time complexity: O(n) , space complexity: O(1)'''