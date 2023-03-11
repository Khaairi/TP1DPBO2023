# Saya Mochamad Khaairi NIM 2106416 mengerjakan TP1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. Aamiin.

# import class lain
from Manusia import Manusia

# inisialisasi class Dosen (inheritance dari class Manusia)
class Dosen(Manusia):
	# atribut
	__nip = ""
	__mastery = ""
	__markers = []
	__laptops = []
	__status = ""

	# constructor (super dari class parent)
	def __init__(self, nik = "", name = "", gender = "", age = 0, nip = "", mastery = "", marker = "", laptop = "", status = ""):
		super().__init__(nik, name, gender, age)
		self.__markers = []
		self.__laptops = []
		self.__nip = nip
		self.__mastery = mastery
		self.__markers.append(marker)
		self.__laptops.append(laptop)
		self.__status = status

	# method setter dan getter
	def setNip(self, nip):
		self.__nip = nip

	def getNip(self):
		return self.__nip

	def setMastery(self, mastery):
		self.__mastery = mastery

	def getMastery(self):
		return self.__mastery

	def setMarkers(self, marker):
		self.__markers.append(marker)

	def getMarkers(self):
		return self.__markers

	def setLaptops(self, laptop):
		self.__laptops.append(laptop)

	def getLaptops(self):
		return self.__laptops

	def setStatus(self, status):
		self.__status = status

	def getStatus(self):
		return self.__status

	def mengajar(self, karakter):
		print(karakter.getName(), "mengajar mata kuliah", self.__mastery, "\n")

	# method untuk memberikan nilai matkul ke mahasiswa
	def beriNilai(self, prodi):
		# caranya sama seperti memberi nilai praktikum pada class Asprak
		# bedanya yaitu pada dosen ada pengecekan apakah mahasiswa yang akan diinput nilainya sudah memiliki nilai praktikum atau belum
		# jika belum maka tidak dapat diinput nilai matkulnya
		flag1 = 0
		flag2 = 0
		flag3 = 0
		print("Input mahasiswa yang akan diberi nilai : ", end="")
		nama = str(input())
		for mahasiswas in prodi.getMahasiswa():
			if(mahasiswas.getName() == nama):
				flag1 = 1
				print("Input mata kuliah yang akan diberi nilai : ", end="")
				matkul = str(input())
				for matkuls in mahasiswas.getMatkul():
					if(matkuls.getNamaMatkul() == matkul):
						flag2 = 1
						print("Masukkan nilai : ", end="")
						nilai = int(input())
						if(matkuls.getNilaiPrak() != 0):
							flag3 = 1
							matkuls.setNilaiMatkul(nilai)
							print("Nilai berhasil diinput!\n")

		if(flag1 == 0):
			print("Mahasiswa tidak tersedia!\n")

		if(flag1 == 1 and flag2 == 0):
			print("Mata kuliah tidak tersedia!\n")

		if(flag1 == 1 and flag2 == 1 and flag3 == 0):
			print("Asisten praktikum belum menginput nilai praktikum!\n")

	# method untuk menampilkan data diri dosen
	def tampil(self, karakter):
		print("=== Data diri ===")
		print("NIK             : ", karakter.getNik())
		print("Nama            : ", karakter.getName())
		print("Jenis Kelamin   : ", karakter.getGender())
		print("Usia            : ", karakter.getAge())
		print("NIP             : ", self.__nip)
		print("Keahlian        : ", self.__mastery)
		print("=== List barang kepemilikan ===")
		i = 0
		print("Spidol : ")
		for spidol in self.__markers:	
			print(str(i + 1), ". ", spidol, sep='')
			i += 1
		i = 0	
		print("Laptop : ")
		for laptop in self.__laptops:	
			print(str(i + 1), ". ", laptop, sep='')
			i += 1
		print("==========================")
		print("")