# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        # slow or rabbit initalize with head node ans it's same with  the Hare or speed
        slow = head
        speed = head
        # loop runs until it reaches null 😶‍🌫️ If there is no cycle
        while speed and speed.next:
            #Increment speed two types
            speed = speed.next.next
            #increment slow only one time
            slow  = slow.next
            # There excits a data in which speed and slow pointers points to the same data then it returns True
            if  speed == slow:
                return True
        #Return False if loop exits
        return False
        #Don't Forget TO UPVOTE😊
        
