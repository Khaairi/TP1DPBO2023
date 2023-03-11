# Saya Mochamad Khaairi NIM 2106416 mengerjakan TP1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. Aamiin.

# inisialisasi class Matkul
class Matkul:
	# atribut
	__namaMatkul = ""
	__nilaiMatkul = 0
	__nilaiPrak = 0

	# constructor
	def __init__(self, namaMatkul = ""):
		self.__nilaiMatkul = 0
		self.__nilaiPrak = 0
		self.__namaMatkul = namaMatkul

	# method setter dan getter
	def setNamaMatkul(self, namaMatkul):
		self.__namaMatkul = namaMatkul

	def getNamaMatkul(self):
		return self.__namaMatkul

	def setNilaiMatkul(self, nilaiMatkul):
		self.__nilaiMatkul = nilaiMatkul

	def getNilaiMatkul(self):
		return self.__nilaiMatkul

	def setNilaiPrak(self, nilaiPrak):
		self.__nilaiPrak = nilaiPrak

	def getNilaiPrak(self):
		return self.__nilaiPrak