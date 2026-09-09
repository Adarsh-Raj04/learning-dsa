from arr import *
from ll import *

nums = [10, 20, 30, 40]


head = build_doubly_linked_list(nums)
print("Original doubly linked list:")
print_doubly_linked_list(head)
print()

print("Inserting at head:")
head = insertion.insert_at_head(head, 5)
print_doubly_linked_list(head)
print()


print("Inserting at tail:")
head = insertion.insert_at_tail(head, 50)
print_doubly_linked_list(head)
print()
