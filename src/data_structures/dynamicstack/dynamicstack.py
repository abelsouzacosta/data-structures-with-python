from typing import Optional
from data_structures.linked_list.linked_list import LinkedList

"""
The dynamic sastack is implemented using a linked list
since arrays has a limited size, using linked lists 
allows to the stack to have variable size
"""


class DynamicStack:
    def __init__(self) -> None:
        self.elements = LinkedList()

    def is_empty(self) -> bool:
        return self.elements.head is None

    def size(self) -> int:
        if self.is_empty():
            return 0
        return self.elements.size

    def push(self, data: int) -> None:
        # insert a element in the head of the linked list
        self.elements.insert_at_head(data)

    def pop(self) -> Optional[int]:
        value = self.elements.get_head()
        if value is not None:
            # updates the list removing the element in the head
            self.elements.delete_from_head()
            return value
        return

    def peek(self) -> Optional[int]:
        return self.elements.get_head()

    # swaps the top two elements in the list
    def swap(self) -> None:
        if self.is_empty():
            return

        top = self.pop()
        second = self.pop()

        if top is not None and second is not None:
            self.push(top)
            self.push(second)

        return
