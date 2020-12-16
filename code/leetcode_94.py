# 94. Binary Tree Inorder Traversal
'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Solution by Yifor
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return  self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

'''time complexity: O(n) , space complexity: O(1)'''

# Recursive Solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        self.inorder(root, answer)
        return answer
            
    def inorder(self, root, answer):
            if root == None:
                return None
            if root.left != None:
                self.inorder(root.left, answer)
            answer.append(root.val)
            if root.right != None:
                self.inorder(root.right, answer)
'''time complexity: O(n) , space complexity: O(n)'''