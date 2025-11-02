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
