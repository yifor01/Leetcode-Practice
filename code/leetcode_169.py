# 169. Majority Element (Easy)
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

# Solution by Yifor
class Solution:
    def majorityElement(self, nums):
        num_dict = {}
        for i in nums:
            if i not in num_dict:
                num_dict[i] = 1
            else:
                num_dict[i] += 1
        majority_count,n = max(num_dict.values()),len(num_dict)
        return  [ list(num_dict.keys())[x] for x in range(n) 
                  if list(num_dict.values())[x] == majority_count ][0]

'''time complexity: O(n) , space complexity: O(n)'''