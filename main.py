# class Laptop
class Laptop:
  # attribute / class varible
  spesifikasi = ['SSD', 'RAM', 'Processor']
  Laptop_menyala = False

  # method contructor / __init_ 
  def __init__ (self, brand , size):
    # asignmet / memasukan ke varible class
    self.brand = brand
    self.size = size

  # menyalakan Laptop
  def menyalakanLaptop(self):
    self.Laptop_menyala = True
    print("Laptop menyala")

  # metode / funsgi menambah Rdan menghapus chanel
  def tambahRAM(self, Jumlah_RAM):
    if(self.Laptop_menyala):
      self.RAM.append(Jumlah_RAM)      
      print("RAM ditambahkan")
    else:
      print("Laptop belum menayala")

 

class App(Laptop):
  # app
  aplikasi = ['VScode','MSoffice']

  # metode / funsgi menambah aplikasi
  def tambahAplikasi(self, nama_aplikasi):
    if(self.Laptop_menyala):
      self.aplikasi.append(nama_aplikasi)      
      print("aplikasi ditambahkan")
    else:
      print("Laptop belum menayala")

  # metode / funsgi menghapus aplikasi
  def hapusApikasi(self, nama_aplikasi):
    if(self.Laptop_menyala):
      self.aplikasi.remove(nama_aplikasi)      
      print("aplikasi dihapus")
    else:
      print("Laptop belum menayala")

# mebuat object dari clas Laptop
Laptop_kuliah = Laptop('Dell', '14inc')
Laptop_kerja= App('Macbook', '15inc')


while True:
  print("1) nyalakan Laptop")
  print("2) tambahkan aplikasi laptop")
  print("3) keluar dari program")
  pilihan = int(input("silahkan masukkan pilihan anda "))
  if(pilihan == 1):
    Laptop_kerja.menyalakanLaptop()
  elif(pilihan == 2):
    print('aplikasi sekarang:')
    print(Laptop_kerja.aplikasi)
    aplikasi = input("silahkan masukan aplikasi: ")
    Laptop_kerja.tambahAplikasi(aplikasi)
    print('aplikasi sekarang:')
    print(Laptop_kerja.aplikasi)
  elif(pilihan == 3):
    print('anda keluar program')
    break
  else:
    print('pilihan tidak ditemukan')
