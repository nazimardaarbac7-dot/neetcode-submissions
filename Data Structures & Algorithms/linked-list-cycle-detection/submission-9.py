# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head 
        d = {}
        while curr:
            if curr in d:
                return True
            d[curr] = True
            curr = curr.next
        return False