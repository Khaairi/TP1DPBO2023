# Saya Mochamad Khaairi NIM 2106416 mengerjakan TP1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. Aamiin.

# import class lain
from Mahasiswa import Mahasiswa

# inisialisasi class AnggotaBEM (inheritance dari class Mahasiswa)
class AnggotaBEM(Mahasiswa):
	# atribut
	__jabatan = ""
	__statusProker = []

	# constructor (super dari class parent)
	def __init__(self, nik = "", name = "", gender = "", age = 0, nim = "", univ = "", faculty = "", major = "", book = "", laptop = "", status = "", jabatan = ""):
		super().__init__(nik, name, gender, age, nim, univ, faculty, major, book, laptop, status)
		self.__jabatan = jabatan

	# method setter dan getter
	def setJabatan(self, jabatan):
		self.__jabatan = jabatan

	def getJabatan(self):
		return self.__jabatan

	# method untuk merancang proker
	def rancangProker(self, BEM):
		# input nama proker
		print("Masukkan nama proker : ", end="")
		proker = str(input())
		# set proker yang ada di bem
		BEM.setProker(proker)
		print("Proker berhasil dirancang!\n")

	# method untuk menjalankan proker
	def jalankanProker(self, BEM):
		i = 0
		flag = 0
		# input nama proker yang akan dijalankan
		print("Masukkan nama proker : ", end="")
		proker = str(input())
		# perulangan untuk mencari proker
		for prokers in BEM.getProker():
			# jika ketemu
			if(prokers == proker):
				# ubah status proker
				self.__statusProker[i] = "2"
				flag = 1
				print("Proker dijalankan!\n")
			i += 1
		if(flag == 0):
			print("Proker tidak tersedia!\n")

	# method untuk menghadiri evaluasi
	def hadiriEvaluasi(self, BEM):
		i = 0
		flag1 = 0
		flag2 = 0
		# input nama proker
		print("Masukkan nama proker : ", end="")
		proker = str(input())
		# perulangan untuk mencari proker
		for prokers in BEM.getProker():
			# jika ketemu
			if(prokers == proker):
				# cek apakah proker sudah dijalankan atau belum
				if(self.__statusProker[i] == "2"):
					# jika sudah maka ubah status
					self.__statusProker[i] = "3"
					flag2 = 1
					print("Proker telah selesai!\n")
				flag1 = 1
			i += 1
		if(flag1 == 0):
			print("Proker tidak tersedia!\n")
		if(flag1 == 1 and flag2 == 0):
			print("Proker belum dijalankan!\n")

	def setStatusProker(self, i):
		self.__statusProker.append(i)

	def getStatusProker(self, i):
		return self.__statusProker[i]
