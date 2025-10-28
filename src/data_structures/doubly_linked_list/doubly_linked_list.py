from typing import Optional
from .node import Node


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.head: Optional[Node] = None

    def insert_at_head(self, data) -> None:
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head.previous = node
        self.head = node
        return

