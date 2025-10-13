from .node import Node
from typing import Optional


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

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

        # Checks if the tail is not empty and then updates the next
        # reference of the current tail and the reference of the list
        # to the tail
        if self.tail is not None:
            self.tail.next = node
            self.tail = node
        else:  # otherwise points both head and tail to the same element
            self.head = node
            self.tail = node

    # insert element after a given element
    def insert_after_element(self, reference, data) -> None:
        node = Node(data)

        if self.head is not None:
            current = self.head

            # Checks if the List is not empty and then
            # goes until find the reference
            while current != None and current.data != reference:
                current = current.next

            """
            Checks if the current node is valid and if the data reference
            stores the reference given
            Then updates the next reference of the current with the
            new node created and set the next reference of the new node
            with the old next reference of the reference given
            """
            if current != None and current.data == reference:
                old_next_element = current.next
                current.next = node
                node.next = old_next_element
            else:  # if the reference is not found then insert at the tail
                self.insert_at_tail(data)
        else:  # if the list is empty then inserts at the head
            self.insert_at_head(data)

    # Removes an element from the tail
    def delete_from_tail(self) -> None:
        if self.head is None:
            raise Exception("List Empty")

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head

            """
            Traverses the list until find the element which the next reference is 
            the tail of the linked list and then updates its next referente to None
            and sets it as the new tail
            """
            while current.next is not None and current.next != self.tail:
                current = current.next

            current.next = None
            self.tail = current

    def delete_from_head(self) -> None:
        if self.head is None:
            raise Exception("List Empty")

        # Takes the second element and sets as the new head
        second_element = self.head.next
        self.head = second_element

    # prints the list in this manner
    def print_list(self) -> None:
        if self.head is None:
            raise Exception("Empty list")

        current = self.head
        while current != None:
            print(current.data)
            current = current.next
