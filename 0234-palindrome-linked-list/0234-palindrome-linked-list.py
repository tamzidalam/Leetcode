# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        
        
        
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
        
#         slow=head
#         fast=head
        
#         while fast and fast.next:
            
#             slow=slow.next
#             fast=fast.next.next
        
        
#         prev=None
#         rev=slow
#         while rev:
#             temp=rev.next
#             rev.next=prev
#             prev=rev
#             rev=temp
            
#         left,right=head,prev
        
#         while right:
#             if left.val != right.val:
#                 return False
#             right=right.next
#             left=left.next
#         return True
        
       