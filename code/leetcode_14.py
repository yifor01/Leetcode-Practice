# 14. Longest Common Prefix (Easy)
'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".


Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Constraints:
    0 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.
'''

# Solution 1 by Yifor
class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        :type strs: List[str]; rtype: str
        """
        sz, ret = zip(*strs), ""
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret
'''time complexity: O(min(l_1,l_2,...,l_n)) , space complexity: O(n)'''

# Solution 2 by Yifor
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        try:
            for word in strs[1:]:
                strs[0] = self.check(strs[0],word)
                if strs[0]=='':
                    break
            return strs[0]
        except:
            return ""
    def check(self,s1,s2):
        for i,(char1,char2) in enumerate(zip(s1,s2)):
            if char1!=char2:
                i-=1
                break
        return s1[:i+1]
'''time complexity: O(n*max(l_i*l_j)) , space complexity: O(1)'''