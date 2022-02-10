# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    На входе два односвязных списка представляющие собой два числа в обратном порядке (1 -> 2 -> 4  =  421)
    Нужно вернуть односвязный список представляющий их сумму в таком же виде.
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first, sec = "", ""
        while l1 or l2:
            if l1:
                first += str(l1.val)
                l1 = l1.next
            if l2:
                sec += str(l2.val)
                l2 = l2.next
        res = reversed(str(int(first[::-1]) + int(sec[::-1])))
        newList = temp = ListNode()
        for i in res:
            temp.next = ListNode(i)
            temp = temp.next
        return newList.next
