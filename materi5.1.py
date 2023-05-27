# TUGAS
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

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        self.length -= 1
        return temp

    def reverse(self):
        new_node = None
        temp = self.head
        while temp is not None:
            next = temp.next
            temp.next = new_node
            new_node = temp
            temp = next
        self.head = new_node


my_linked_list = LinkedList(None)


def menu():
    while True:
        print("="*30)
        print("=======MENU LINKED LIST=======")
        print("="*30)
        print("1. Buat Linked List Baru")
        print("2. Append")
        print("3. Prepend")
        print("4. Pop")
        print("5. Pop First")
        print("6. Insert")
        print("7. Remove")
        print("8. Reverse")
        print("9. Print List")
        print("10. Exit")
        print("="*30)

        pilihan = int(input("Masukan Pilihan Menu: "))
        if pilihan == 1:
            my_linked_list = LinkedList(
                input("Masukan angka untuk membuat Linked list baru: "))
        elif pilihan == 2:
            my_linked_list.append(input("Masukan angka untuk append: "))
        elif pilihan == 3:
            my_linked_list.prepend(input("Masukan angka untuk prepend: "))
        elif pilihan == 4:
            print("Sebelum di pop")
            my_linked_list.print_list()
            my_linked_list.pop()
            print("Sesudah di pop")
            my_linked_list.print_list()
        elif pilihan == 5:
            print("sebelum di pop first")
            my_linked_list.print_list()
            my_linked_list.pop_first()
            print("Sesudah di pop first")
            my_linked_list.print_list()
        elif pilihan == 6:
            my_linked_list.print_list()
            my_linked_list.insert(int(input("Masukan index yang ingin di insert: ")), input(
                "Masukan angka baru untuk insert: "))
        elif pilihan == 7:
            my_linked_list.print_list()
            my_linked_list.remove(
                int(input("Masukan index yang ingin diremove: "))).value
        elif pilihan == 8:
            my_linked_list.reverse()
        elif pilihan == 9:
            my_linked_list.print_list()
        else:
            print("Terimakasih telah menggunakan menu ini")
            break


menu()
