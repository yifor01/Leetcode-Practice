# 206. Reverse Linked List
'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. 
Could you implement both?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = None

# Solution by Yifor
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:        
        def reverse(head,ans=None):
            if not head:
                return ans
            next = head.next
            head.next = ans
            return reverse(next,head)
        return reverse(head,None)

'''time complexity: O(n) , space complexity: O(1)'''
