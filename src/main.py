from data_structures.dynamicstack.dynamicstack import DynamicStack
from data_structures.linked_list.linked_list import LinkedList

ds = DynamicStack()
ds.push(1)
ds.push(2)
ds.push(3)
ds.push(4)
ds.elements.print_list()
ds.swap()
ds.elements.print_list()
print(ds.elements.size)

ll = LinkedList()
ll.insert_at_head(2)
ll.insert_at_head(3)
ll.insert_at_head(4)
ll.insert_at_head(5)
ll.insert_at_head(6)
ll.insert_at_head(7)
ll.print_list()
print("Calling reverse until")
ll.reverse_until(4)
ll.print_list()
