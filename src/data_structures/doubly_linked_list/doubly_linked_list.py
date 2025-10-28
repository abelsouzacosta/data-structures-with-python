from typing import Optional
from .node import Node


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

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

    def print_list(self) -> None:
        if self.head is None:
            print("[]")
            return

        current = self.head
        while current is not None:
            if current.next is None:
                print(f"{current.data}\n")
            else:
                print(f"{current.data} <-> ", end="")
            current = current.next

    def print_list_reverse(self) -> None:
        if self.head is None:
            print("[]")
            return

        current = self.tail
        while current is not None:
            if current.previous is None:
                print(f"{current.data}")
            else:
                print(f"{current.data} <-> ", end="")
            current = current.previous
