# 171. Excel Sheet Column Number. (Easy)
'''
Given a column title as appear in an Excel sheet, 
return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
'''

# Solution by Yifor
class Solution:
    def titleToNumber(self, s: str) -> int:
        s = s.upper()
        worddict = {}
        pos,n,times,ans = 1,len(s),0,0
        for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            worddict[i] = pos
            pos+=1
        for i in range(n):
            ans += worddict[s[n-i-1]]*(26**times)
            times+=1
        return ans
		
'''time complexity: O(n) , space complexity: O(1)'''