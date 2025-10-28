from typing import Optional
from .node import Node


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def insert_at_empty_list(self, data) -> None:
        node = Node(data)
        self.head = node
        self.tail = node
        return

    def insert_at_head(self, data) -> None:
        node = Node(data)

        if self.head is None:
            self.insert_at_empty_list(data)
            return

        node.next = self.head
        self.head.previous = node
        self.head = node
        return

    def insert_at_tail(self, data) -> None:
        node = Node(data)

        if self.tail is None:
            self.insert_at_empty_list(data)
            return

        self.tail.next = node
        node.previous = self.tail
        self.tail = node

    def delete_from_head(self) -> None:
        if self.head is None:
            return

        # unary list
        if self.head.next is None:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.previous = None

    def delete_from_tail(self) -> None:
        if self.tail is None:
            return

        # unary list
        if self.tail.previous is None:
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.previous
        self.tail.next = None

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
