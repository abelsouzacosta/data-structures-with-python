from typing import Optional


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Optional[Node | None] = None
        self.previous: Optional[Node | None] = None
