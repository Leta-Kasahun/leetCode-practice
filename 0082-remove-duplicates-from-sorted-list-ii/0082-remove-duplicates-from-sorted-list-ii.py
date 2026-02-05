# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next=next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        seen={}
        curr=head
        
        while curr:
            if curr.val in seen:
                seen[curr.val]+=1
            else:
                seen[curr.val]=1
            curr=curr.next
        curr=head
        prev=None    
        while curr:
            if seen[curr.val]>1:
                if prev:
                    prev.next=curr.next
                else:
                    head=curr.next
            else:
                prev=curr
            curr=curr.next
        return head                                      