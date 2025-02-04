# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        temp=headA
        a=0
        while temp:
            a+=1
            temp=temp.next
        temp=headB
        b=0
        while temp:
            b+=1
            temp=temp.next
        if a>b:
            for i in range(a-b):
                headA=headA.next
        else:
            for i in range(b-a):
                headB=headB.next
        while headA and headB:
            if headA==headB:
                return headA
            else:
                headA=headA.next
                headB=headB.next
        return None
        
