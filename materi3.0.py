# EROR KARENA PENULISAN INDENTASI SALAH
# my_list = [1,2,3]
# print(my_list[0])
# print(my_list[2])
# print(my_list[4])

# INDETASI BENAR
my_list = [1, 2, 3]
print(my_list[0])
print(my_list[1])
print(my_list[2])

a = "Hello"
print(a)
print(len(a))
for x in "banana":
    print(x)

print(a[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])
print(len(thistuple))

# one item tuple
thistuple = ("apple", )
print(thistuple)

# Not a Tupple
thistuple = ("apple")
print(thistuple)

# Different types of set in Pyhton
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# create a set using set constructor
# set of strings
book_set = set(("Harry Potter", "Angels and Demons", "Atlas Shrugged"))
print(book_set)

# LATIHAN
barang = []


def inputBarang():
    global barang
    inputBarang = str(input("Masukan Nama Barang : "))
    barang.append(inputBarang)


def lihatKeranjang():
    global barang
    for i in barang:
        print(i)


def hapusBarang():
    global barang
    cariBarang = str(input("Masukan nama Barang: "))
    for i in barang:
        if i == cariBarang:
            barang.remove(i)
            print(barang)
            break


while True:
    print("""
    1. Tambah Barang Ke keranjang
    2. Lihat Keranjang
    3. Hapus Barang dari Keranjang
    4. Keluar Program"""
        )
    pilihan = int(input("Masukan pilihan Menu: "))

    if pilihan == 1:
        inputBarang()
    elif pilihan == 2:
        lihatKeranjang()
    elif pilihan == 3:
        hapusBarang()
    else:
        print("Tidak ada pilihan menu")
        break
