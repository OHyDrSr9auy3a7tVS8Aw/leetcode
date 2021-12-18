from typing import Optional as Opt


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next: Opt["Node"] = None

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"


class MyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self) -> str:
        return repr(self.head)

    def get(self, index: int) -> int:
        curr = self.head

        if curr is None:
            return -1

        if index == 0:
            return curr.val

        try:
            for _ in range(index):
                curr = curr.next

            return curr.val
        except AttributeError:
            return -1

    def addAtHead(self, val: int) -> None:
        old_head = self.head
        self.head = Node(val)
        self.head.next = old_head

    def addAtTail(self, val: int) -> None:
        curr = self.head

        if curr is None:
            self.head = Node(val)
            return

        while curr.next is not None:
            curr = curr.next

        curr.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head

        if curr is None:
            if index == 0:
                self.head = Node(val)
                return
            else:
                return

        if index == 0:
            self.addAtHead(val)
            return

        try:
            for _ in range(index):
                prev, curr = curr, curr.next

            prev.next = Node(val)
            prev.next.next = curr
        except AttributeError:
            return

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head

        if curr is None:
            return

        if index == 0:
            self.head = curr.next
            return

        try:
            for _ in range(index):
                prev, curr = curr, curr.next

            prev.next = curr.next
        except AttributeError:
            return