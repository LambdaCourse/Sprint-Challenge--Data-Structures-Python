class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


# Stretch Goal # 
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cur = None
        self.storage = DoublyLinkedList()  # not using list per read-me instructions

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)

        else:
            if not self.cur or not self.cur.next:
                self.cur = self.storage.head

            else:
                self.cur = self.cur.next
            self.cur.value = item

    def get(self):
        buffer_container = []

        node = self.storage.head
        while node is not None:
            buffer_container.append(node.value)
            node = node.next

        return buffer_container
