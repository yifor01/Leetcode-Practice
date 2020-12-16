# 242. Valid Anagram
'''
Given two strings s and t , 
write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? 
How would you adapt your solution to such case?
'''

# Solution by Yifor
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1,str2 = dict(),dict()
        n1,n2 = len(s),len(t)        
        if n1!=n2:
            return False
        for i in range(n1):
            if s[i] not in str1:
                str1[s[i]] = 1
            else:
                str1[s[i]] +=1
            if t[i] not in str2:
                str2[t[i]] = 1
            else:
                str2[t[i]] +=1
        return str1==str2

'''time complexity: O(n) , space complexity: O(n)'''