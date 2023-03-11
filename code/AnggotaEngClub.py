# Saya Mochamad Khaairi NIM 2106416 mengerjakan TP1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. Aamiin.

# import dari class lain
from Mahasiswa import Mahasiswa

# inisialisasi class AnggotaEngClub
class AnggotaEngClub(Mahasiswa):
	# atribut
	__jabatan = ""
	__TOEFLScore = ""

	# consturctor (dengan super dari class parent)
	def __init__(self, nik = "", name = "", gender = "", age = 0, nim = "", univ = "", faculty = "", major = "", book = "", laptop = "", status = "", jabatan = "", TOEFLScore = ""):
		super().__init__(nik, name, gender, age, nim, univ, faculty, major, book, laptop, status)
		self.__jabatan = jabatan
		self.__TOEFLScore = TOEFLScore

	# methid setter dan getter
	def setJabatan(self, jabatan):
		self.__jabatan = jabatan

	def getJabatan(self):
		return self.__jabatan

	def setTOEFLScore(self, TOEFLScore):
		self.__TOEFLScore = TOEFLScore

	def getTOEFLScore(self):
		return self.__TOEFLScore

	def belajarEng(self, karakter):
		print(karakter.getName(), "is practicing his/her english!\n")

	# method untuk merancang proker
	def rancangProker(self, EngClub):
		# masukkan nama proker
		print("Masukkan nama proker : ", end="")
		proker = str(input())
		EngClub.setProker(proker)
		print("Proker berhasil dirancang!\n")
