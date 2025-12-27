class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")


def reverse_linked_list(linked_list):
    """Reverses a singly linked list by changing links between nodes."""
    prev = None
    current = linked_list.head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    linked_list.head = prev
    return linked_list


def get_middle(head):
    """Finds the middle node using two-pointer technique."""
    if not head:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def sorted_merge(left, right):
    """Merges two sorted lists into one sorted list."""
    if not left:
        return right
    if not right:
        return left

    if left.data <= right.data:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)
    return result


def merge_sort(head):
    """Recursive merge sort for linked list nodes."""
    if not head or not head.next:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    return sorted_merge(left, right)


def merge_sort_linked_list(linked_list):
    """Sorts a singly linked list using merge sort algorithm."""
    linked_list.head = merge_sort(linked_list.head)
    return linked_list


def merge_two_sorted_lists(list1, list2):
    """Merges two sorted singly linked lists into one sorted list."""
    merged_list = LinkedList()
    merged_list.head = sorted_merge(list1.head, list2.head)
    return merged_list


if __name__ == "__main__":
    print("=== Reversing a singly linked list ===")
    ll = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        ll.append(value)
    print("Original list:")
    ll.print_list()
    reverse_linked_list(ll)
    print("Reversed list:")
    ll.print_list()

    print("\n=== Sorting a singly linked list (merge sort) ===")
    unsorted_ll = LinkedList()
    for value in [64, 34, 25, 12, 22, 11, 90]:
        unsorted_ll.append(value)
    print("Unsorted list:")
    unsorted_ll.print_list()
    merge_sort_linked_list(unsorted_ll)
    print("Sorted list:")
    unsorted_ll.print_list()

    print("\n=== Merging two sorted lists ===")
    list1 = LinkedList()
    for value in [1, 3, 5, 7]:
        list1.append(value)
    list2 = LinkedList()
    for value in [2, 4, 6, 8]:
        list2.append(value)
    print("First sorted list:")
    list1.print_list()
    print("Second sorted list:")
    list2.print_list()
    merged = merge_two_sorted_lists(list1, list2)
    print("Merged sorted list:")
    merged.print_list()
