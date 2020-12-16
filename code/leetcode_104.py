# 104. Maximum Depth of Binary Tree
'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],
return its depth = 3.
'''

# Solution by Yifor
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
## example = [3,9,20,None,None,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.right = None
root.left.left = None
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

class Solution:
    def maxDepth(self, root):
        if not root:   
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1

'''time complexity: O(n) , space complexity: O(1)'''