class Node:
    def __init__(self, nomor_rekam_medis, nama_pasien, tanggal_lahir, alamat, nomor_telepon, keluhan):
        self.nomor_rekam_medis = nomor_rekam_medis
        self.nama_pasien = nama_pasien
        self.tanggal_lahir = tanggal_lahir
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon
        self.keluhan = keluhan
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print("\nNomor Rekam Medis    :", temp.nomor_rekam_medis)
            print("Nama Pasien           :", temp.nama_pasien)
            print("Tanggal Lahir         :", temp.tanggal_lahir)
            print("Alamat                :", temp.alamat)
            print("Nomor Telepon         :", temp.nomor_telepon)
            print("Keluhan               :", temp.keluhan)
            temp = temp.next

    def push(self, nomor_rekam_medis, nama_pasien, tanggal_lahir, alamat, nomor_telepon, keluhan):
        new_node = Node(nomor_rekam_medis, nama_pasien,
                        tanggal_lahir, alamat, nomor_telepon, keluhan)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print("\nNomor Rekam Medis    :", temp.nomor_rekam_medis)
            print("Nama Pasien           :", temp.nama_pasien)
            print("Tanggal Lahir         :", temp.tanggal_lahir)
            print("Alamat                :", temp.alamat)
            print("Nomor Telepon         :", temp.nomor_telepon)
            print("Keluhan               :", temp.keluhan)
            temp = temp.next

    def enqueue(self, new_node):
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


antrian_pasien = Queue()
loket1 = Stack()
loket2 = Stack()
loket3 = Stack()

# BAGIAN FUNGSI


def buat_antrian_pasien():
    nomor_rekam_medis = input("Nomor Rekam Medis              : ")
    nama_pasien = input("Masukkan Nama Pasien           : ")
    tanggal_lahir = input("Masukkan Tanggal Lahir Pasien  : ")
    alamat = input("Masukkan Alamat Pasien         : ")
    nomor_telepon = input("Masukkan Nomor telepon Pasien  : ")
    keluhan = input("Masukkan Keluhan Pasien        : ")
    new_node = Node(nomor_rekam_medis, nama_pasien,
                    tanggal_lahir, alamat, nomor_telepon, keluhan)
    antrian_pasien.enqueue(new_node)
    print("Pasien dengan nomor {} telah mengambil nomor antrian".format(
        nomor_rekam_medis))


def tampil_seluruh_pasien():
    print("============DAFTAR ANTRIAN PASIEN============")
    antrian_pasien.print_queue()
    print("="*45)

# PANGGIL PASIEN KE LOKET


def panggil_loket1():
    new_node = antrian_pasien.dequeue()
    if loket1.height == 0:
        print("Memanggil Pasien menuju loket 1")
        loket1.push(new_node.nomor_rekam_medis, new_node.nama_pasien, new_node.tanggal_lahir,
                    new_node.alamat, new_node.nomor_telepon, new_node.keluhan)
    else:
        print("Tidak ada pasien yang mengantri! ")


def panggil_loket2():
    new_node = antrian_pasien.dequeue()
    if loket1.height == 0:
        print("Memanggil Pasien menuju loket 2")
        loket2.push(new_node.nomor_rekam_medis, new_node.nama_pasien, new_node.tanggal_lahir,
                    new_node.alamat, new_node.nomor_telepon, new_node.keluhan)
    else:
        print("Tidak ada pasien yang mengantri! ")


def panggil_loket3():
    new_node = antrian_pasien.dequeue()
    if loket1.height == 0:
        print("Memanggil Pasien menuju loket 3")
        loket3.push(new_node.nomor_rekam_medis, new_node.nama_pasien, new_node.tanggal_lahir,
                    new_node.alamat, new_node.nomor_telepon, new_node.keluhan)
    else:
        print("Tidak ada pasien yang mengantri! ")

# LIHAT HISTORY


def history_loket1():
    print("======HISTORY ANTRIAN PASIEN DI LOKET 1======")
    loket1.print_stack()
    print("="*45)


def history_loket2():
    print("======HISTORY ANTRIAN PASIEN DI LOKET 2======")
    loket2.print_stack()
    print("="*45)


def history_loket3():
    print("======HISTORY ANTRIAN PASIEN DI LOKET 3======")
    loket3.print_stack()
    print("="*45)


# BAGIAN MENU
def menu():
    while True:
        print("="*45)
        print("=====Sistem Antrian Pendaftaran Berobat=====")
        print("1. Ambil Nomor Urut Antrian")
        print("2. Tampil Seluruh Pasien dalam Antrian")
        print("3. Panggil Pasien ke loket 1")
        print("4. Panggil Pasien ke loket 2")
        print("5. Panggil Pasien ke loket 3")
        print("6. Lihat History Pelayanan loket 1")
        print("7. Lihat History Pelayanan loket 2")
        print("8. Lihat History Pelayanan loket 3")
        print("9. Keluar Program")
        print("="*45)

        pilihan = int(input("Masukkan Pilihan Menu: "))

        if pilihan == 1:
            buat_antrian_pasien()
        elif pilihan == 2:
            tampil_seluruh_pasien()
        elif pilihan == 3:
            panggil_loket1()
        elif pilihan == 4:
            panggil_loket2()
        elif pilihan == 5:
            panggil_loket3()
        elif pilihan == 6:
            history_loket1()
        elif pilihan == 7:
            history_loket2()
        elif pilihan == 8:
            history_loket3()
        elif pilihan == 9:
            print("Terimakasih telah menggunakan porgram ini!")
            break
        else:
            print("tidak ada pilihan menu")
            break


menu()
