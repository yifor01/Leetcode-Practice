# 172. Factorial Trailing Zeroes (Easy)
'''
Given an integer n, return the number of trailing zeroes in n!.
Follow up: Could you write a solution that works in logarithmic time complexity?

Example 1:
    Input: n = 3
    Output: 0
    Explanation: 3! = 6, no trailing zero.

Example 2:
    Input: n = 5
    Output: 1
    Explanation: 5! = 120, one trailing zero.

Example 3:
    Input: n = 0
    Output: 0

Constraints:
    1 <= n <= 104
'''

# Solution by Yifor
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return sum([n // 5 ** x for x in range(1, 6)])

'''time complexity: O(1) , space complexity: O(1)'''