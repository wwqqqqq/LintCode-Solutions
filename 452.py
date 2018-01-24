#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
@param: head: a ListNode
@param: val: An integer
@return: a ListNode
"""
    def removeElements(self, head, val):
        while head != None and head.val == val:
            head = head.next
        if head == None:
            return None
        node = head.next
        p = head
        while node != None:
            if node.val == val:
                if node == head:
                    head = head.next
                else:
                    p.next = node.next
            else:
                p = p.next
            node = node.next
        return head
'''
if __name__ == "__main__":
    ln = ListNode()
'''