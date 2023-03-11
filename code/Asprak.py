# Saya Mochamad Khaairi NIM 2106416 mengerjakan TP1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. Aamiin.

# import class lain
from Mahasiswa import Mahasiswa

# inisialisasi class Asprak (inheritance dari class Mahasiswa)
class Asprak(Mahasiswa):
	# atribut
	__namaPrak = ""

	# constructor (super dari class parent)
	def __init__(self, nik = "", name = "", gender = "", age = 0, nim = "", univ = "", faculty = "", major = "", book = "", laptop = "", status = "", namaPrak = ""):
		super().__init__(nik, name, gender, age, nim, univ, faculty, major, book, laptop, status)
		self.__namaPrak = namaPrak

	# method setter dan getter
	def setNamaPrak(self, namaPrak):
		self.__namaPrak = namaPrak

	def getNamaPrak(self):
		return self.__namaPrak

	def mengajar(self, karakter):
		print(karakter.getName(), "mengajar praktikum", self.__namaPrak, "\n")

	# method untuk memberikan nilai praktikum kepada mahasiswa lainnya
	# composite dari class Mahasiswa
	def beriNilai(self, prodi):
		# note : mahasiswa pada class Prodi berisi kumpulan dari class Mahasiwa, class Asprak, class AnggotaBEM dan class AnggotaEngClub yang semunya termasuk ke dalam "mahasiswa"
		# variabel penanda
		flag1 = 0
		flag2 = 0
		# input nama mahasiswa yang akan diberi nilai
		print("Input mahasiswa yang akan diberi nilai : ", end="")
		nama = str(input())
		# perulangan untuk mencari mahasiswa yang dimaksud dari kumpulan object mahasiswa di class Prodi
		for mahasiswa in prodi.getMahasiswa():
			# jika mahasiswa terdapat di class Prodi
			if(mahasiswa.getName() == nama):
				flag1 = 1
				# input nama mata kuliah yang akan diinput nilai praktikum
				print("Input nama mata kuliah yang akan diberi nilai : ", end="")
				matkul = str(input())
				# perulangan untuk mencari nama mata kuliah yang dimaksud dari kumpulan object matkul pada class Mahasiswa
				for matkuls in mahasiswa.getMatkul():
					# jika ketemu
					if(matkuls.getNamaMatkul() == matkul):
						flag2 = 1
						# input nilai praktikum
						print("Masukkan nilai : ", end="")
						nilaiPrak = int(input())
						# set nilai praktikum ke class Matkul
						matkuls.setNilaiPrak(nilaiPrak)
						print("Nilai praktikum berhasil diinput!\n")

		# jika mahasiswa tidak ada di list mahasiwa di class Prodi 
		if(flag1 == 0):
			print("Mahasiswa tidak tersedia!\n")

		# jika mahasiswa ada tapi matkulnya tidak ada
		if(flag1 == 1 and flag2 == 0):
			print("Mata kuliah tidak tersedia!\n")

	# method untuk memberikan tugas praktikum ke semua mahasiswa
	def beriTugas(self, karakter, prodi):
		# input nama tugasnya
		print("Masukkan nama tugas : ", end="")
		__tugas = str(input())
		# perulangan untuk men-set tugas ke semua mahasiswa dari list mahasiwa di class Prodi
		for mahasiswa in prodi.getMahasiswa():
			mahasiswa.setTugasPrak(__tugas)
		
		print(karakter.getName(), "sebagai asisten praktikum", self.__namaPrak, "memberikan tugas praktikum ke semua mahasiswa!\n")