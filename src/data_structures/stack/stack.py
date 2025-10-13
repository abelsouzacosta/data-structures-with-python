class Stack:
    def __init__(self) -> None:
        self.items = []

    # checks if the stack is empty
    def is_empty(self) -> bool:
        return len(self.items) == 0

    # insert a element at the top of the stack
    def push(self, element: int) -> None:
        self.items.append(element)

    # removes and return the element at the top of the array
    def pop(self) -> int:
        if self.is_empty():
            raise Exception("Empty Stack")
        # takes the last element of the array
        top = self.items[-1]
        # delete the element
        del self.items[-1]

        """
        Python provides the method pop for lists
        but since the idea here is to learn data structures then 
        all the process above is made manually, but in 'real life'
        you can just use the method pop: self.items.pop()
        """
        return top

