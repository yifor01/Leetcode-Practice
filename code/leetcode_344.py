

# 0344. Reverse String (Easy)
'''
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

'''

# Solution by Yifor
def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    n = len(s)
    for i in range(n//2):
        s[i],s[n-i-1] = s[n-i-1],s[i]

'''time complexity: O(n/2) , space complexity: O(1)'''