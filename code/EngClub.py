# Saya Mochamad Khaairi NIM 2106416 mengerjakan TP1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. Aamiin.

# inisialisasi class EngClub
class EngClub:
	# atribut
	__ketua = ""
	__anggota = []
	__proker = []

	# constructor (untuk anggota merupakan composite dari class AnggotaEngClub)
	def __init__(self, anggota, ketua = ""):
		self.__ketua = ketua
		self.__anggota.append(anggota)

	# method untuk setter dan getter
	def setKetua(self, ketua):
		self.__ketua = ketua

	def getKetua(self):
		return self.__ketua

	def setAnggota(self, anggota):
		self.__anggota.append(anggota)

	def getAnggota(self):
		return self.__anggota

	def setProker(self, proker):
		self.__proker.append(proker)

	def getProker(self):
		return self.__proker