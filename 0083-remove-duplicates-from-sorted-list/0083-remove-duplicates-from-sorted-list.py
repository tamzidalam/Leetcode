# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        current=head
        p2=head
        
        while p2:
            if current.val != p2.val:
                current.next=p2
                current=current.next
              
            p2=p2.next
        
        current.next=None
        return head
            