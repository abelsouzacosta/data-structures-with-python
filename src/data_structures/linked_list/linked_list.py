from .node import Node


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # Insert an element at the head
    def insert_at_head(self, data) -> None:
        node = Node(data)

        if self.head is not None:
            old_head = self.head
            self.head = node
            node.next = old_head
        else:
            self.head = node
            self.tail = node

