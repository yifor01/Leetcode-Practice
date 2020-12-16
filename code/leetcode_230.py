# 230. Kth Smallest Element in a BST (Medium)

'''
Question:
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
'''

# Solution by Yifor
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        aa = [root.val]
        root = [root]
        while root:
            if root[0].left:
                root.append(root[0].left)
                aa.append(root[0].left.val)
            if root[0].right:
                root.append(root[0].right)
                aa.append(root[0].right.val)
            del root[0]
        return sorted(aa)[k-1]

'''time complexity: O(nlog(n)) , space complexity: O(n)'''