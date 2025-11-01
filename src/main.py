from data_structures.stack.stack import Stack
from data_structures.linked_list.linked_list import LinkedList
from data_structures.doubly_linked_list.doubly_linked_list import DoublyLinkedList

stack = Stack()

stack.push(5)
stack.push(15)
stack.push(25)
stack.push(35)
stack.push(45)

print(stack.pop())  # 45
print(stack.pop())  # 35

my_list = LinkedList()

my_list.insert_at_head(1)
my_list.insert_at_head(2)
my_list.insert_at_head(3)
my_list.insert_at_head(4)
my_list.insert_at_head(5)
my_list.insert_at_tail(10)
my_list.insert_after_reference(6, 5)

my_list.print_list()

print("Removing elements")

my_list.delete_from_head()
my_list.delete_from_tail()
my_list.delete_from_tail()
my_list.delete_from_tail()

my_list.print_list()
print("Remove a chosen element")
my_list.delete_element(4)

my_list.print_list()

new_list = LinkedList()

new_list.insert_at_head(1)
new_list.insert_at_head(2)
new_list.insert_at_head(3)
new_list.insert_at_head(4)
new_list.insert_at_head(5)
new_list.insert_at_head(6)
new_list.insert_at_head(7)

print("New list: ")
new_list.print_list()
print("Reversing list")
new_list.reverse()
new_list.print_list()

dl = DoublyLinkedList()
dl.insert_at_head(1)
dl.insert_at_head(2)
dl.insert_at_head(3)
dl.insert_at_head(4)
dl.insert_at_tail(5)
dl.insert_at_tail(6)
dl.insert_at_tail(7)
dl.print_list()
dl.delete_from_head()
dl.print_list()
dl.delete_from_tail()
dl.print_list()
dl.insert_after_reference(2, 1000)
dl.print_list()

another_list = LinkedList()
another_list.insert_at_head(1)
another_list.insert_at_head(1)
another_list.insert_at_head(1)
another_list.insert_at_head(2)
another_list.insert_at_head(3)
another_list.insert_at_head(4)
another_list.print_list()
another_list.remove_duplicates()
another_list.print_list()

dll = DoublyLinkedList()
dll.insert_at_head(1)
dll.insert_at_head(2)
dll.insert_at_head(3)
dll.insert_at_head(6)
dll.insert_at_head(10)
dll.insert_at_tail(10)
dll.insert_after_reference(1000, 1)
dll.print_list()
