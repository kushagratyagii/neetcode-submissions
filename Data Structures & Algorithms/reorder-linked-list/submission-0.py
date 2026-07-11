# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head.next

        #Splitting linkeed list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first_half,second_half = head, slow.next
        
        slow.next = None
        prev = None
        #reversing linked list

        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp

        #Now merging #because it is smaller linked list
        while prev:
              temp1 = first_half.next
              temp2 = prev.next
              first_half.next = prev
              prev.next = temp1
              first_half,prev = temp1,temp2


