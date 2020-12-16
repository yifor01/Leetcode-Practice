#387. First Unique Character in a String (Easy)
'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''

# Solution by Yifor
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s=='':
            return -1
        firstword,words = {},{}
        for idx,word in enumerate(s):
            if word in words:
                words[word] += 1
            else:
                words[word],firstword[word] = 1,idx
        for i in words.keys():
            if words[i] == 1:
                return firstword[i]
        return -1

'''time complexity: O(n) , space complexity: O(1)'''