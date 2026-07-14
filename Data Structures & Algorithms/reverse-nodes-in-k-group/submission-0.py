# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev = dummy # 1->|2->3|->4 groupPrev will store 1
        while True:
            kth = self.getkth(groupPrev,k)
            if not kth :
                break
            groupNext = kth.next # 1->|2->3|->4 groupNext will store 4
            
            #Now reversing the group
            p,c = kth.next,groupPrev.next # Current group ka first node reverse hone ke baad tail ban jaata hai. Us tail ko group ke next node (kth.next) se connect karna hota hai. Isliye prev = kth.next rakhte hain.
            while c!= groupNext:
                t = c.next
                c.next = p
                p = c
                c = t
            temp = groupPrev.next
            groupPrev.next = kth# next groupPrev yehi element h starting waala 
            groupPrev = temp
        return dummy.next



    
    
    def getkth(self,curr,k):
        while curr and k>0:
            curr = curr.next
            k -= 1
        return curr

