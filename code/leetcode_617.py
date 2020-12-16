# 617. Merge Two Binary Trees (Easy)

'''
Given two binary trees and imagine that when you put one of them to cover the other, 
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, 
then sum node values up as the new value of the merged node. Otherwise, 
the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
 

Note: The merging process must start from the root nodes of both trees.
'''
# Definition for a binary tree node.
# =============================================================================
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 
# t1 = TreeNode(1)
# t1.left = TreeNode(3)
# t1.right = TreeNode(2)
# t1.left.left = TreeNode(5)
# t1.left.right = None
# t1.right.left = None
# t1.right.right = None
# 
# t2 = TreeNode(5)
# t2.left = TreeNode(6)
# t2.right = TreeNode(6)
# t2.left.left = None
# t2.left.right = TreeNode(3)
# t2.right.left = None
# t2.right.right = TreeNode(2)
# =============================================================================

# Solution by Yifor
class Solution(object):
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            root = TreeNode(t1.val+t2.val)
            root.left = self.mergeTrees(t1.left,t2.left)
            root.right = self.mergeTrees(t1.right,t2.right)
            return root
        else:
            return t1 or t2

'''time complexity: O(n) , space complexity: O(n)'''