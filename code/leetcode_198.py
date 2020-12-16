

# 0198. House Robber (Easy)
'''
Question:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Input: [1,2,3,1]
Output: 4
Explanation: 
Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
'''

# Solution by Yifor
def rob( nums ):
    l = len(nums)
    if l == 0:
        return 0
    if l == 1:
        return nums[0]
    a1,a2 = nums[0] , max(nums[0],nums[1]) 
    for i in range(2,l):
        a1,a2 = a2,max(a1+nums[i],a2)
    return max(a1,a2)

'''time complexity: O(n) , space complexity: O(1)'''