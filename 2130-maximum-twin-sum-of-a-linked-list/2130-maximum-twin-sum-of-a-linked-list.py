# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        maxx=float(-inf)
        
        numbers=[]
        
        while head:
            numbers.append(head.val)
            head=head.next
        

        p1=0
        p2=len(numbers)-1
        
        while p1<p2:
            maxx=max(maxx,numbers[p1]+numbers[p2])
            p1+=1
            p2-=1
        
        print(maxx)
        return maxx
        