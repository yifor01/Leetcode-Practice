# 238. Product of Array Except Self
'''
Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of space complexity analysis.)
'''

# Solution by Yifor
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n,ans,zero = len(nums),1,0
        for i in range(n):
            if nums[i]:
                ans *= nums[i]
            else:
                zero+=1
        for i in range(n):
            if not nums[i]:
                if zero -1 >0:
                    nums[i] = 0
                else:
                    nums[i] = int(ans)
            else:
                if zero>0:
                    nums[i] = 0
                else:
                    nums[i] = int(ans/nums[i])
        return nums
'''time complexity: O(n) , space complexity: O(1)'''

# Best Solution

# 思路:
# 正反遍历数组
# 由于res[i] = (x0 * x1 * ... * xi-1) * (xi+1 * .... * xn-1)，因此执行两趟循环：
# 第一趟正向遍历数组，计算x0 ~ xi-1的乘积
# 第二趟反向遍历数组，计算xi+1 ~ xn-1的乘积

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [1] * size
        
        # Forward through
        left = 1
        for i in range(size):
            res[i] *= left
            left *= nums[i]

        # Backward through
        right = 1
        for i in range(size-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res  

'''time complexity: O(n) , space complexity: O(1)'''
