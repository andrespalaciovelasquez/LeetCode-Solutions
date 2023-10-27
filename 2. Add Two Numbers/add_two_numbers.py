class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        _sum = x + y + carry
        carry = _sum // 10

        current.next = ListNode(_sum % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry > 0:
        current.next = ListNode(carry)

    return dummy_head.next

# Example usage:
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = addTwoNumbers(l1, l2) # Output: 7 -> 0 -> 8 ->

# Print the result
while result:
    print(result.val, end=" -> ")
    result = result.next
print()

l3 = ListNode(0)
l4 = ListNode(0)
result2 = addTwoNumbers(l3, l4) # Output: 0 ->

while result2:
    print(result2.val, end=" -> ")
    result2 = result2.next
print()

l5 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l6 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
result3 = addTwoNumbers(l5, l6) # Output: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1 ->

while result3:
    print(result3.val, end=" -> ")
    result3 = result3.next

