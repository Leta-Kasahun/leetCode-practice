# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def __init__(self):
        self.head=None
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        Head=ListNode(0)
        Head.next=head
        curr=Head
        while curr.next:
            if curr.next.val==val:
                curr.next=curr.next.next
            else:

              curr=curr.next    
        return Head.next       