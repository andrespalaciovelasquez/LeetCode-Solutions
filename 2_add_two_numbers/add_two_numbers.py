from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 is not None or l2 is not None or carry != 0:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        column_sum = x + y + carry
        carry = column_sum // 10
        current.next = ListNode(column_sum % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry > 0:
        current.next = ListNode(carry)

    return dummy_head.next


def print_linked_list(head: Optional[ListNode]) -> None:
    values = []

    while head:
        values.append(head.val)
        head = head.next

    print(values)


# Example 1:
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = add_two_numbers(l1, l2)  # Output: 7 -> 0 -> 8 ->
print_linked_list(result)  # Output: [7, 0, 8]

# Example 2:
l3 = ListNode(0)
l4 = ListNode(0)
result2 = add_two_numbers(l3, l4)  # Output: 0 ->
print_linked_list(result2)  # Output: [0]

# Example 3:
l5 = ListNode(
    9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
)
l6 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
result3 = add_two_numbers(l5, l6)  # Output: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1 ->
print_linked_list(result3)  # Output: [8, 9, 9, 9, 0, 0, 0, 1]
