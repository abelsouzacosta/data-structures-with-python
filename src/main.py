from data_structures.stack.stack import Stack
from data_structures.linked_list.linked_list import LinkedList

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
my_list.insert_after_element(5, 6)

my_list.print_list()

print("Removing elements")

my_list.delete_from_head()

my_list.print_list()
