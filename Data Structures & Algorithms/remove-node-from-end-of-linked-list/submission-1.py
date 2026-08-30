# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head 
        prev =None 
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            # reversed 
        first = prev 
        if n == 1 :
            first = first.next
        else:
            curr = prev 
            for _ in range(n-2):
                curr = curr.next 
            curr.next = curr.next.next 
        
        curr = first
        prev =None 
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        

