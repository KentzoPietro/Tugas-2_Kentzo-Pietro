print("Selamat Datang")
nama_kontak = ["Fawwaz","John"]
nomer_kontak = ["08123456789","08987654321"]
def menu():
 print("1.Daftar Kontak")
 print("2.Tambah Kontak")
 print("3.Keluar")

def kontaks():
 print("Daftar Kontak: ")
 for i in range(len(nama_kontak)):
   print("Nama: {}".format(nama_kontak[i]))
   print("Nomer Telepon: {}".format(nomer_kontak[i]))

def tambah():
  nama = input("Nama : ")
  nomer =input("Kontak : ")
  nama_kontak.append(nama)
  nomer_kontak.append(nomer)
  print("Kontak berhasil ditambahkan")
while True :
    menu()
    menus = int(input("Silahkan pilih menu : "))
    if menus == 1:
        kontaks()

    elif menus == 2:
        tambah()

    elif menus == 3:
      print("Terima Kasih dan selamat jumpa")
      break
    else:
        print("Menu tidak tersedia")
