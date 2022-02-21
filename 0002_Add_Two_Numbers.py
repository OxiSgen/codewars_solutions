# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    На входе два односвязных списка представляющие собой два числа в обратном порядке (1 -> 2 -> 4  =  421)
    Нужно вернуть односвязный список представляющий их сумму в таком же виде.
    Гаранитруется, что список представляет собой число без лидирующих нулей.
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first, sec = "", ""  # Создаём две строки для записи в них наших чисел
        while l1 or l2: # Проходимся по двум спискам и записываем цифры в строки
            if l1:
                first += str(l1.val)
                l1 = l1.next
            if l2:
                sec += str(l2.val)
                l2 = l2.next
        res = reversed(str(int(first[::-1]) + int(sec[::-1]))) # Складываем перевёрнутые в нужную сторону числа, переводим их в строку и опять разворачиваем
        newList = temp = ListNode() # Создаём два указателя на список. С одним работаем (temp), а другой возвращаем (newList.next)
        for i in res: 
            temp.next = ListNode(i) 
            temp = temp.next # Используем указатель temp для заполнения списка.
            # для строки "708" temp на каждой итерации будет выглядить следуюем образом:
            # ListNode{val: 7, next: None}
            # ListNode{val: 0, next: None}
            # ListNode{val: 8, next: None}
        # newList    =   ListNode{val: 0, next: ListNode{val: 7, next: ListNode{val: 0, next: ListNode{val: 8, next: None}}}}.
        # первый элемент служебный, по этому возвращяем .next
        return newList.next
    
     """
     Вариант 2 из решений других людей. Вместо того, чтобы отдельно создавать числа и генерировать новый список, делаем всё сразу. Идея как при сложении в столбик.
     """
     def addTwoNumbers(self, l1, l2):
            carry = 0;
            res = n = ListNode(0);
            while l1 or l2 or carry:
                if l1:
                    carry += l1.val
                    l1 = l1.next;
                if l2:
                    carry += l2.val; # carry - сумма двух цифр из одного разряда первого и второго числа.
                    l2 = l2.next;
                carry, val = divmod(carry, 10) # carry - целая часть от деления, которую мы переносим в слеющий разряд. val - то, что мы оставляем в данном разряде.
                n.next = n = ListNode(val);
            return res.next;
