# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        c1=l1
        c2=l2
        dummy=ListNode(0)
        carry=0
        pointer=dummy
        
        while c1  or c2 :
            
            v1=c1.val if c1 else 0
            v2=c2.val if c2 else 0
            
            temp=v1 + v2 + carry
            
            if temp > 9:
                temp = temp % 10
                pointer.next=ListNode(temp)
                carry=1
                temp=0
                
            elif temp<10:
                pointer.next=ListNode(temp)
                temp=0
                carry=0
            
            pointer=pointer.next
            
            c1=c1.next if c1 else None
            c2=c2.next if c2 else None
        
        
        ### This edge case is for 8+7= 15,999+99 =1098,the last carry that remains 
        if carry == 1:
            pointer.next=ListNode(carry)
            
        return dummy.next
        