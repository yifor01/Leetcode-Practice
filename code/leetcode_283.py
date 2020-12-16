# 283. Move Zeroes (Easy)
'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

# Solution by Yifor
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n,count,start = len(nums),0,0
        while True:
            try:
                if not nums[start]:
                    del nums[start]
                    count+=1
                else:
                    start+=1
            except:
                break
        nums+=[0]*count

'''time complexity: O(n**2) , space complexity: O(1)'''

# Best Solution 
class Solution:
    def moveZeroes(self, nums):
        count = nums.count(0)
        nums[:] = [x for x in nums if x!=0]
        nums+=[0]*count