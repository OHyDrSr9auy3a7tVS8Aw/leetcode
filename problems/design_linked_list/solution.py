from typing import Optional as Opt


class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev: Opt["Node"] = None
        self.next: Opt["Node"] = None

    def __repr__(self) -> str:
        try:
            next_val = self.next.val
        except AttributeError:
            next_val = None
        try:
            prev_val = self.prev.val
        except AttributeError:
            prev_val = None

        return f"{prev_val} -> {self.val} -> {next_val}"


class MyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self) -> str:
        out = []
        curr = self.head

        while curr is not None:
            out.append(repr(curr))
            curr = curr.next

        return str(out)

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

        if old_head is None:
            self.head = Node(val)
            return

        self.head = Node(val)
        self.head.next = old_head
        old_head.prev = self.head

    def addAtTail(self, val: int) -> None:
        curr = self.head

        if curr is None:
            self.head = Node(val)
            return

        while curr.next is not None:
            curr = curr.next

        new_node = Node(val)
        curr.next = new_node
        new_node.prev = curr

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

            new_node = Node(val)
            prev.next = new_node
            new_node.next = curr

            curr.prev = new_node
            new_node.prev = prev

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
            curr.next.prev = prev
        except AttributeError:
            return