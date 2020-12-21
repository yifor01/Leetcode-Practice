# 125. Valid Palindrome (Easy)
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note:
    For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
    Input: "A man, a plan, a canal: Panama"
    Output: true

Example 2:
    Input: "race a car"
    Output: false

Constraints:
    s consists only of printable ASCII characters.
'''

# Solution by Yifor
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s, word = s.lower(), ''
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        for char in s:
            if char in chars:
                word += char
        n2 = int(len(word) / 2)
        return word[:n2] == word[:-(n2 + 1):-1]

'''time complexity: O(n) , space complexity: O(n)'''