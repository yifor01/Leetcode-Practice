# 118. Pascal's Triangle
'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

# Solution by Yifor
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(numRows):
            tmp = [1]
            if output:
                for idx, val in enumerate(output[-1][:-1]):
                    tmp.append(output[-1][idx] + output[-1][idx+1])
                tmp += [1]
            output.append(tmp)
        return output
'''time complexity: O(n!) , space complexity: O(n)'''