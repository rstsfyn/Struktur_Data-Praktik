class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print()

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # ##def bubble sort ketika menjalankan swap value
    # def bubble_sort(self):
    #   if self.head is None:
    #     return
    #   for i in range(self.length - 1, 0, -1):
    #     temp = self.head
    #     for j in range(i):
    #       if temp .next is not None and temp.value > temp.next.value:
    #         self.swap_value(temp)
    #       temp = temp.next
    #     print('Proses: ', end = " ")
    #     self.print_list_horizon()

    # def bubble sort ketika menjalankan swap node
    def bubble_sort(self):
        if self.head is None or self.head.next is None:
            return
        for i in range(self.length - 1, 0, -1):
            prev_node = None
            temp = self.head
            while temp and temp.next:
                next_node = temp.next
                if temp.value > next_node.value:
                    self.swap_node(prev_node, temp, next_node)
                    temp, next_node = next_node, temp
                prev_node = temp
                temp = temp.next

    def print_list_horizon(self):
        listku = []
        temp = self.head
        while temp is not None:
            listku.append(temp.value)
            temp = temp.next
        print(listku)

    # def swap_value(self, node):
    #   temp = node.value
    #   node.value = node.next.value
    #   node.next.value = temp

    def swap_node(self, prev_node, node1, node2):
        if node1 == node2:
            return
        if prev_node is None:
            self.head = node2
        else:
            prev_node.next = node2

        node1.next = node2.next
        node2.next = node1
        if self.head == node1:
            self.head = node2
        if self.tail == node2:
            self.tail = node1
        print("Proses: ", end=" ")
        self.print_list_horizon()


my_linked_list = LinkedList(5)
my_linked_list.append(2)
my_linked_list.append(2)
my_linked_list.append(0)
my_linked_list.append(4)
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.append(0)
my_linked_list.append(8)
my_linked_list.append(2)

while True:
    print("**************M E N U*****************")
    print("1. Print List Horizon")
    print("2. Bubble Sort")
    print("3. Keluar")
    pilihan = int(input("Masukkan pilihan menu: "))

    if pilihan == 1:
        print("Print List Horizon")
        my_linked_list.print_list_horizon()
    elif pilihan == 2:
        print("===========Proses Swap Node===========")
        my_linked_list.bubble_sort()
    elif pilihan == 3:
        print("Terimakasih telah menggunakan Menu ini")
        break
    else:
        print("pilihan menu tidak ada!")
        break
