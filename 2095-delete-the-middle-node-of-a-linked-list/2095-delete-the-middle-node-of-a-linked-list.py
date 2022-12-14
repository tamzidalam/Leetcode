# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev=head
        slow=head
        fast=head
        flag=0
        while fast and fast.next:
            flag=1
            prev=slow
            slow=slow.next
            fast=fast.next.next
        
        prev.next=slow.next
        
        if flag == 0:
            
            head=None
            return head
        return head
        