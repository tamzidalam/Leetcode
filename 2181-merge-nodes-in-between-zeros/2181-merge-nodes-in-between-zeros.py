# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode(0,head)
        p1=dummy
        p2=head.next
        
        summ=0
        
        while p2 and p2.next:
            
            summ+=p2.val
            #print(p2.val)
            if p2.next.val == 0:
                print(summ)
                p2.val=summ
                p1.next=p2
                p1=p1.next
                p2=p2.next
                summ=0
            
            p2=p2.next
        
        p1.next=None
        return dummy.next
                
            
            
            
            
            
        