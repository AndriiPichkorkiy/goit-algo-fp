class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def revers(self):
        if self.head is None or \
           self.head.next is None:
            return

        prev = self.head
        next = self.head.next
        prev.next = None
        while next:
            prev, next.next, next = next, prev, next.next
        self.head = prev

    def sort(self):
        if self.head is None or \
           self.head.next is None:
            return

        # сортування бульбашкой
        is_sorted = False
        while not is_sorted:
            is_sorted = True

            cur = self.head
            next = self.head.next
            while next is not None:
                if next.data < cur.data:
                    is_sorted = False
                    cur.data, next.data = next.data, cur.data

                cur, next = next, next.next


def merge_lists(*lists: LinkedList):
    new_llist = LinkedList()

    pointers = []  # type: list[Node]
    for list in lists:
        if list is not None and list.head is not None:
            pointers.append(list.head)

    while len(pointers):
        smallest = pointers[0]
        temp_point = 0
        for i in range(1, len(pointers)):
            node = pointers[i]
            if node.data < smallest.data:
                smallest = node
                temp_point = i

        new_llist.insert_at_end(smallest.data)
        pointers[temp_point] = pointers[temp_point].next

        if pointers[temp_point] is None:
            pointers.remove(pointers[temp_point])

    return new_llist


if __name__ == "__main__":
    # створюємо список
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(25)
    llist.insert_at_beginning(20)
    llist.insert_at_beginning(15)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(5)

    print("Зв'язний спискок до реверсу")
    llist.print_list()

    print("\nЗв'язний спискок після реверсу")
    llist.revers()
    llist.print_list()

    print("\nСортування")
    llist.sort()
    llist.print_list()

    print("\nЗлиття")

    # створюємо другий список
    llist2 = LinkedList()
    llist2.insert_at_beginning(125)
    llist2.insert_at_beginning(120)
    llist2.insert_at_beginning(115)
    llist2.insert_at_beginning(110)
    llist2.insert_at_beginning(15)

    # злиття списків
    merged_list = merge_lists(llist2, llist)
    merged_list.print_list()
