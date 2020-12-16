# 20. Valid Parentheses (Easy)
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Example 4:
    Input: s = "([)]"
    Output: false

Example 5:
    Input: s = "{[]}"
    Output: true

Constraints:
    1 <= s.length <= 10**4
    s consists of parentheses only '()[]{}'.
'''


# Solution 1 by Yifor
class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s) % 2:
            for i in range(len(s) // 2):
                s = s.replace('()', '')
                s = s.replace('[]', '')
                s = s.replace('{}', '')
            n = len(s)
            return s[:n // 2] == s[n // 2::-1] if n else True
        else:
            return False
'''time complexity: O(n**2) , space complexity: O(1)'''


# Solution 2 by Yifor
class Solution:
    def isValid(self, s: str) -> bool:
        reverse_map = {'(': ')', '[': ']', '{': '}'}
        watch = []
        if (s[0] in reverse_map) and (not len(s) % 2):
            for ele in s:
                if ele in ['(', '[', '{']:
                    watch.append(ele)
                else:
                    try:
                        if reverse_map.get(watch[-1]) != ele:
                            return False
                        else:
                            watch.pop()
                    except:
                        return False
            return watch == []
        else:
            return False
'''time complexity: O(n) , space complexity: O(n)'''