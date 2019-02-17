# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        #不需要以下几句,因为有while l1 and l2
        if l1 == None and l2 != None:
            return l2
        elif l1 != None and l2 == None:
            return l1
        elif l1 == None and l2 == None:
            return None
        else:
        """
        head = ListNode(0)
        first_node=head
        while l1 and l2:
            if l1.val<=l2.val:
            	head.next=l1
            	l1=l1.next
            else:
            	head.next=l2
            	l2=l2.next
            #下面这句是关键!移动指针,使head形成一个链表,而不是一个节点指来指去
            head=head.next
        if l1:
            head.next=l1
        else:
            head.next=l2
        return first_node.next

