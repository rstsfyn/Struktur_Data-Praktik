# TUGAS

class Node:
    def __init__(self, nomor_pegawai, nama_pegawai, usia, posisi):
        self.nomor_pegawai = nomor_pegawai
        self.nama_pegawai = nama_pegawai
        self.usia = usia
        self.posisi = posisi
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, nomor_pegawai, nama_pegawai, usia, posisi):
        new_node = Node(nomor_pegawai, nama_pegawai, usia, posisi)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def prepend(self, nomor_pegawai, nama_pegawai, usia, posisi):
        new_node = Node(nomor_pegawai, nama_pegawai, usia, posisi)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def set_value(self, index, nomor_pegawai, nama_pegawai, usia, posisi):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.nomor_pegawai = nomor_pegawai
        temp.nama_pegawai = nama_pegawai
        temp.usia = usia
        temp.posisi = posisi

    def remove_pegawai(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index == 0:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
        else:
            for i in range(index):
                temp = temp.next
            temp.prev.next = temp.next
            if temp is not None:
                temp.next.prev = temp.prev
            else:
                self.tail = temp.prev
        self.length -= 1

    def print_pegawai(self):
        temp = self.head
        while temp is not None:
            print("=====Daftar Info Pegawai dalam Doubly Linked List=====")
            print("No. Pegawai    :", temp.nomor_pegawai)
            print("Nama Pegawai   :", temp.nama_pegawai)
            print("Usia           :", temp.usia)
            print("Posisi         :", temp.posisi)
            print("="*54)
            temp = temp.next


my_doubly_linked_list = DoublyLinkedList()


def menu():
    while True:
        print("===============Sistem Informasi Pegawai===============")
        print("1. Tambah Pegawai Baru (Prepend)")
        print("2. Tampil Seluruh Data Pegawai")
        print("3. Ubah Data Pegawai")
        print("4. Hapus Data Pegawai")
        print("5. Keluar Program")
        print("="*54)
        pilihan = int(input("Masukkan Pilihan Menu: "))

        if pilihan == 1:
            nomor_pegawai = input("Masukkan Nomor Pegawai: ")
            nama_pegawai = input("Masukkan Nama Pegawai: ")
            usia = int(input("Masukkan Usia Pegawai: "))
            posisi = input("Masukkan Posisi Pegawai: ")
            my_doubly_linked_list.prepend(
                nomor_pegawai, nama_pegawai, usia, posisi)
        elif pilihan == 2:
            my_doubly_linked_list.print_pegawai()
        elif pilihan == 3:
            index = int(input("Masukan index yang ingin diedit: "))
            if my_doubly_linked_list:
                nomor_pegawai = input("Masukan Nomor Pegawai: ")
                nama_pegawai = input("Masukan Nama Pegawai: ")
                usia = int(input("Masukan usia pegawai: "))
                posisi = input("Masukan Posisi Pegawai: ")
                my_doubly_linked_list.set_value(
                    index, nomor_pegawai, nama_pegawai, usia, posisi)
                print("Data diubah!")
            else:
                print("Index tidak ada")
        elif pilihan == 4:
            index = int(input("Masukkan Index Pegawai yang ingin Dihapus: "))
            my_doubly_linked_list.remove_pegawai(index)
        elif pilihan == 5:
            print("Terimakasih telah menggunakan menu ini:)")
            break
        else:
            print("Pilihan Menu tidak ada")


menu()
