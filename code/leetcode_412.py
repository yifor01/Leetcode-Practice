# 412. Fizz Buzz
'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''

# Solution by Yifor
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [''] * n
        for i in range(n):
            if (i+1) % 3 ==0:
                ans[i] += "Fizz"
            if (i+1) % 5 ==0:
                ans[i] += "Buzz"
                continue 
            if (i+1) % 3 >0:
                ans[i] += str(i+1)
        return ans

'''time complexity: O(n) , space complexity: O(n)'''