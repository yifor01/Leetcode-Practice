# 83. Remove Duplicates from Sorted List (Easy)
'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''

# Solution by Yifor
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return head

'''time complexity: O(n) , space complexity: O(n)'''