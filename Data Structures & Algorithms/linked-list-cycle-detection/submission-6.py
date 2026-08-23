# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = defaultdict(int)
        curr = head
        while curr:
            d[curr] += 1 
            if d[curr] > 1 :
                return True
            else:
                curr = curr.next
        return False
            