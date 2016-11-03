class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = None
        tail = None

        while l1 or l2 or carry:
        	tnode = 0
        	if l1:
        		tnode += l1.val
        		l1 = l1.next
        	if l2:
        		tnode += l2.val
        		l2 = l2.next
        	tnode += carry
        	carry = 0

        	if tnode >= 10:
        		carry = tnode // 10
        		tnode = tnode % 10

        	if head is None:
        		head = ListNode(tnode)
        		tail = head
        	else:
        		tail.next = ListNode(tnode)
        		tail = tail.next

        return head