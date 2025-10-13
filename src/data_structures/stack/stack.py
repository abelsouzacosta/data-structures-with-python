class Stack:
    def __init__(self) -> None:
        self.items = []

    # checks if the stack is empty
    def is_empty(self) -> bool:
        return len(self.items) == 0

