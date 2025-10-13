from .node import Node


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # Insert an element at the head
    def insert_at_head(self, data) -> None:
        node = Node(data)

        """
        Checks if head is not empty and then inserts 
        the new node at the head and sets the old head
        as the next element of the node
        """

        if self.head is not None:
            old_head = self.head
            self.head = node
            node.next = old_head
        else:
            self.head = node
            self.tail = node

    # insert a element at the tail of the linked list
    def insert_at_tail(self, data) -> None:
        node = Node(data)

        if self.tail is not None:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    # prints the list in this manner
    def print_list(self) -> None:
        if self.head is None:
            raise Exception("Empty list")

        current = self.head
        while current != None:
            print(current.data)
            current = current.next
