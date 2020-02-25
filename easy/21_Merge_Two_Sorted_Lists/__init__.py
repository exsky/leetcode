# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mr = []
        while True:
            if l1:
                if l2:
                    if l1.val < l2.val:
                        mr.append(l1.val)
                        l1 = l1.next
                    else:
                        mr.append(l2.val)
                        l2 = l2.next
                else: # l2 is empty but l1
                    mr.append(l1.val)
                    l1 = l1.next
            else: # l1 is empty, but dont know l2
                if l2:
                    mr.append(l2.val)
                   l2 = l2.next
                else: # l2 is also empty
                    return self.list2ListNode(mr)
    def list2ListNode(self, li):
        ans = None  # Head
        while li:
            x = ListNode(li.pop(-1))    # From tail to head
            x.next = ans
            ans = x
        return ans 
