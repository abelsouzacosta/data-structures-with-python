from .node import Node
from typing import Optional


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def get_head(self) -> Optional[int | None]:
        if self.head is None:
            return
        return self.head.data

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
            self.size += 1
        else:
            self.head = node
            self.tail = node
            self.size += 1

    # insert a element at the tail of the linked list
    def insert_at_tail(self, data) -> None:
        node = Node(data)

        # Checks if the tail is not empty and then updates the next
        # reference of the current tail and the reference of the list
        # to the tail
        if self.tail is not None:
            self.tail.next = node
            self.tail = node
            self.size += 1
        else:  # otherwise points both head and tail to the same element
            self.head = node
            self.tail = node
            self.size += 1

    # insert element after a given element
    def insert_after_reference(self, data: int, reference: int) -> None:
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
                self.size += 1
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
            self.size -= 1
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
            self.size -= 1

    # Removes an element from the head of the list
    def delete_from_head(self) -> None:
        if self.head is None:
            raise Exception("List Empty")

        # Takes the second element and sets as the new head
        second_element = self.head.next
        self.head = second_element
        self.size -= 1

    def delete_element(self, reference: int) -> None:
        if self.head is None:
            raise Exception("List Empty")

        if self.head.data == reference:
            self.delete_from_head()

        if self.tail is not None and self.tail.data == reference:
            self.delete_from_tail()

        current = self.head

        """
        Traverses the list until the node where the next element is the reference given
        then updates the current node 'next' reference with the 'next' reference of the 
        node to be deleted
        """
        while current.next is not None and current.next.data != reference:
            current = current.next

        node_to_delete = current.next
        if node_to_delete is not None:
            current.next = node_to_delete.next
            self.size -= 1

    # Reverses the LinkedList
    def reverse(self) -> None:
        previous = None
        current = self.head
        old_head = self.head

        while current is not None:
            # stores the next element
            next = current.next
            # points the next reference to the previous position
            current.next = previous
            # updates the previous reference to the current
            previous = current
            # updates the current reference to the next
            current = next

        self.head = previous
        self.tail = old_head

    # will remove duplicates from the list
    def remove_duplicates(self):
        if self.head is None or self.head.next is None:
            return

        current = self.head
        while current is not None:
            runner = current
            while runner.next is not None:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    # prints the list in this manner
    def print_list(self) -> None:
        if self.head is None:
            print("[]")

        current = self.head
        while current is not None:
            if current.next is None:
                print(f"{current.data}")
            else:
                print(f"{current.data} -> ", end="")
            current = current.next
