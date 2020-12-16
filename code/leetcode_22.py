# 22. Generate Parentheses
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

# Solution by Yifor
class Solution:
    def generateParenthesis(self, n) :
        def permute(a,b,init='',ans=[]) :
            print(a,b)
            if a : 
                permute(a-1,b,init+'(')
            if b>a:
                permute(a,b-1,init+')')
            if not b:
                ans.append(init) # or 'ans += init,' # 讓list吃到''
            return ans
        return permute(n,n,'')

'''time complexity: O(2**n) , space complexity: O(n)'''