class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkList(object):
    """"
    init the head node
    """

    def __init__(self):
        self.head = None

    def insertNode(self, data):
        newNode = ListNode(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -->")
            current = current.next


if __name__ == "__main__":
    l1 = LinkList()
    l1.insertNode(1)
    l1.insertNode(2)
    l1.insertNode(3)
    l1.print()
