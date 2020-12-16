# 287. Find the Duplicate Number (Medium)
'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

# Solution 1 by Yifor
class Solution: # with modify the array  
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]

'''time complexity: O(nlog(n)) , space complexity: O(1)'''

# Solution 2 by Yifor
class Solution: # with not modify the array  
	def findDuplicate(self,nums):
		slow,fast,finder=0,0,0
		while True:
			slow = nums[slow]
			fast = nums[nums[fast]]
			print(slow,fast,finder)
			if fast==slow:
				while finder!=slow:
					finder = nums[finder]
					slow = nums[slow]
					print(slow,fast,finder)
				print(slow,fast,finder)
				return finder
				
'''time complexity: O(n) , space complexity: O(1)'''

