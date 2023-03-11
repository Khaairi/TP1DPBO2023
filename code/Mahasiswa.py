# Saya Mochamad Khaairi NIM 2106416 mengerjakan TP1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. Aamiin.

# import class lain
from Manusia import Manusia
from Matkul import Matkul

# inisialisasi class Mahasiswa (inheritance dari class Manusia)
class Mahasiswa(Manusia):
	# atribut
	__nim = ""
	__univ = ""
	__faculty = ""
	__major = ""
	__books = []
	__laptops = []
	__status = ""
	__tugasPrak = []
	__matkul = []

	# constructor (menggunakan super dari constructor parent)
	def __init__(self, nik = "", name = "", gender = "", age = 0, nim = "", univ = "", faculty = "", major = "", book = "", laptop = "", status = ""):
		super().__init__(nik, name, gender, age)
		self.__books = []
		self.__laptops = []
		self.__matkul = []
		self.__nim = nim
		self.__univ = univ
		self.__faculty = faculty
		self.__major = major
		self.__books.append(book)
		self.__laptops.append(laptop)
		self.__status = status

	# method setter dan getter
	def setNim(self, nim):
		self.__nim = nim

	def getNim(self):
		return self.__nim

	def setUniv(self, univ):
		self.__univ = univ

	def getUniv(self):
		return self.__univ

	def setFaculty(self, faculty):
		self.__faculty = faculty

	def getFaculty(self):
		return self.__faculty

	def setMajor(self, major):
		self.__major = major

	def getMajor(self):
		return self.__major

	def setBooks(self, book):
		self.__books.append(book)

	def getBooks(self):
		return self.__books

	def setLaptops(self, laptop):
		self.__laptops.append(laptop)

	def getLaptops(self):
		return self.__laptops

	def setStatus(self, status):
		self.__status = status

	def getStatus(self):
		return self.__status

	def setTugasPrak(self, tugasPrak):
		self.__tugasPrak.append(tugasPrak)

	def getTugasPrak(self):
		return self.__tugasPrak

	# untuk matkul berupa composite dari class Matkul
	def setMatkul(self, namaMatkul):
		temp = Matkul(namaMatkul)
		self.__matkul.append(temp)

	def getMatkul(self):
		return self.__matkul

	def study(self, karakter):
		print(karakter.getName(), "is studying\n")

	# method untuk menampilkan data diri mahasiswa beserta nilai dari matkul yang dikontrak
	def tampil(self, karakter):
		print("=== Data diri ===")
		print("NIK             : ", karakter.getNik())
		print("Nama            : ", karakter.getName())
		print("Jenis Kelamin   : ", karakter.getGender())
		print("Usia            : ", karakter.getAge())
		print("NIM             : ", self.__nim)
		print("Universitas     : ", self.__univ)
		print("Fakultas        : ", self.__faculty)
		print("Program Studi   : ", self.__major)
		print("Status          : ", self.__status)
		print("")
		print("=== List barang kepemilikan ===")
		i = 0
		print("Buku : ")
		for buku in self.__books:	
			print(str(i + 1), ". ", buku, sep='')
			i += 1
		i = 0	
		print("Laptop : ")
		for laptop in self.__laptops:	
			print(str(i + 1), ". ", laptop, sep='')
			i += 1
		print("")
		i = 0
		print("=== Daftar Nilai ===")
		for matkuls in self.__matkul:
			print(str(i+1), ". ", matkuls.getNamaMatkul(), sep='')
			print("   Nilai Keseluruhan : ", matkuls.getNilaiMatkul(), sep='')
			print("   Nilai Praktikum   : ", matkuls.getNilaiPrak(), sep='')
			i += 1
		print("==========================")
		print("")

	# method untuk menampilkan list tugas praktikum
	def tampilTugas(self):
		i = 0
		print("=== List Tugas ===")
		for tugas in self.__tugasPrak:
			print(str(i + 1), ". ", tugas, sep='')
			i += 1
		print("==========================")
		print("")