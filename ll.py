class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None

    def build_from_list(self, values):
        if not values:
            return

        self.head = self.Node(values[0])
        current = self.head

        for value in values[1:]:
            current.next = self.Node(value)
            current = current.next
        return self.head

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


# --------- use of LinkedList class to build and print a linked list ----------#
# linked_list = LinkedList()
# linked_list.build_from_list([1, 2, 3, 4, 5])
# linked_list.print_list()


# ------------ Building a linked list from a list of values ----------#
def build_linked_list(values):
    if not values:
        return None

    head = Node(values[0])
    current = head

    for value in values[1:]:
        current.next = Node(value)
        current = current.next

    return head


# -------- printing a linked list ----------#
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# ---------- reversing a linked list using recursion ----------#
def reverse_linked_list(head):
    if head is None or head.next is None:
        return head

    new_head = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None

    return new_head


# ----------- Reversing a linked list using iteration ----------#
def reverse_linked_list_iterative(head):
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


# ---------- Finding the middle of a linked list ----------#
def find_middle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


# ------------ detecting a cycle in a linked list ----------#
def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# ----------- delete a node in a linked list given only access to that node ----------#
def delete_node(node):
    if node is None or node.next is None:
        raise Exception("Cannot delete the last node or a null node with this method.")

    next_node = node.next
    node.value = next_node.value
    node.next = next_node.next


# ------------ insert at ith position in a linked list ----------#
def insert_at_position(head, position, value):
    new_node = Node(value)

    if position == 0:
        new_node.next = head
        return new_node

    current = head
    for _ in range(position - 1):
        if current is None:
            raise Exception("Position out of bounds.")
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


# ---------- remove nth node from the end of a linked list ----------#
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Move first n+1 steps ahead
    for _ in range(n + 1):
        if first is None:
            raise Exception("n is larger than the length of the linked list.")
        print(first.value)  # Debugging line to check the value of first
        first = first.next

    # Move first to the end, maintaining the gap
    while first is not None:
        print(
            f"First: {first.value}, Second: {second.value}"
        )  # Debugging line to check the values of first and second
        first = first.next
        second = second.next

    # Remove the nth node from end
    print(
        f"Removing node with value: {second.next.value}"
    )  # Debugging line to check which node is being removed
    second.next = second.next.next

    return dummy.next


# --------- length of linked list ----------#
def length_of_linked_list(head):
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next
    return length


# ---------- search for a value in a linked list ----------#
def search_linked_list(head, target):
    current = head
    while current is not None:
        if current.value == target:
            return True
        current = current.next
    return False


# -------- get mid of linked list ----------#
def get_mid_of_linked_list(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


# ---------------------------------------------------------------------------------------------------------------
#                          Doubly Linked List Implementation
# ----------------------------------------------------------------------------------------------------------------


class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


# ------------- Building a doubly linked list from a list of values ----------#
def build_doubly_linked_list(values):
    if not values:
        return None

    head = DoublyNode(values[0])
    current = head

    for value in values[1:]:
        new_node = DoublyNode(value)
        current.next = new_node
        new_node.prev = current
        current = new_node

    return head


# ------------ printing a doubly linked list ----------#
def print_doubly_linked_list(head):
    current = head
    while current is not None:
        print(current.value, end=" <-> ")
        current = current.next
    print("None")


# ----------- get tail of doubly linked list ----------#
def get_tail_of_doubly_linked_list(head):
    current = head
    while current is not None and current.next is not None:
        current = current.next
    return current


# ------------- print backward doubly linked list ----------#
def print_backward_doubly_linked_list(tail):
    current = tail
    while current is not None:
        print(current.value, end=" <-> ")
        current = current.prev
    print("None")


# ----------- Insertion in doubly Linked List -----------#
class insertion:
    @staticmethod
    def insert_at_head(head, value):
        new_node = DoublyNode(value)
        new_node.next = head
        if head is not None:
            head.prev = new_node
        return new_node

    @staticmethod
    def insert_at_tail(head, value):
        new_node = DoublyNode(value)
        if head is None:
            return new_node

        tail = get_tail_of_doubly_linked_list(head)
        tail.next = new_node
        new_node.prev = tail
        return head

    @staticmethod
    def insert_at_position(head, position, value):
        if position == 0:
            return insertion.insert_at_head(head, value)

        current = head
        for _ in range(position - 1):
            if current is None:
                raise Exception("Position out of bounds.")
            current = current.next

        if current is None:
            raise Exception("Position out of bounds.")

        new_node = DoublyNode(value)
        new_node.next = current.next
        new_node.prev = current

        if current.next is not None:
            current.next.prev = new_node

        current.next = new_node
        return head


# ----------- Deletion in doubly Linked List -----------#
class deletion:
    @staticmethod
    def delete_at_head(head):
        if head is None:
            return None
        new_head = head.next
        if new_head is not None:
            new_head.prev = None
        return new_head

    @staticmethod
    def delete_at_tail(head):
        if head is None:
            return None

        tail = get_tail_of_doubly_linked_list(head)
        if tail.prev is not None:
            tail.prev.next = None
        else:
            return None  # List had only one node

        return head

    @staticmethod
    def delete_at_position(head, position):
        if position == 0:
            return deletion.delete_at_head(head)

        current = head
        for _ in range(position):
            if current is None:
                raise Exception("Position out of bounds.")
            current = current.next

        if current is None:
            raise Exception("Position out of bounds.")

        if current.prev is not None:
            current.prev.next = current.next
        if current.next is not None:
            current.next.prev = current.prev

        return head


# ---------------------------------------------------------------------------------------------------------------
#                          Circular Linked List Implementation
# ----------------------------------------------------------------------------------------------------------------


class CircularNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# ---------- Building a circular linked list from a list of values ----------#
def build_circular_linked_list(values):
    if not values:
        return None

    head = CircularNode(values[0])
    current = head

    for value in values[1:]:
        current.next = CircularNode(value)
        current = current.next

    current.next = head  # Make it circular
    return head


# ----------- printing a circular linked list ----------#
def print_circular_linked_list(head):
    if head is None:
        print("None")
        return

    current = head
    while True:
        print(current.value, end=" -> ")
        current = current.next
        if current == head:
            break
    print("(back to head)")
