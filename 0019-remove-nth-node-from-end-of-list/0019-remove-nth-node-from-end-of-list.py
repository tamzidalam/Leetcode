# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
                
        node=head
        prev=head
        count=0
        
        flag=0
        
        while True:
            if node is None:
                break
            node=node.next
            
            count+=1
        
        if count == 1:
            return None
        
        node=head    
        count=count-n
        
        i=0
        if count == 0:
            head = head.next
        while True:
            flag=1
            if i == count:
                prev.next= node.next
                break
            prev=node
            node=node.next
            
            i+=1
        
        
        return head
            