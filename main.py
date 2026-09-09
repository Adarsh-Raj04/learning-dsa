from arr import *
from ll import *

nums = [10, 20, 30, 40]

head = build_circular_linked_list(nums)
print_circular_linked_list(head)


# ----- check if cyclic
print("Is cyclic:", has_cycle(head))
