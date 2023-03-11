# Saya Mochamad Khaairi NIM 2106416 mengerjakan TP1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. Aamiin.

# inisialisasi class BEM
class BEM:
	# atribut
	__ketua = ""
	__anggota = []
	__proker = []

	# constructor (untuk anggota berupa composite dari class AnggotaBEM)
	def __init__(self, anggota, ketua = ""):
		self.__ketua = ketua
		self.__anggota.append(anggota)

	# method setter dan getter
	def setKetua(self, ketua):
		self.__ketua = ketua

	def getKetua(self):
		return self.__ketua

	def setAnggota(self, anggota):
		self.__anggota.append(anggota)

	def getAnggota(self):
		return self.__anggota

	# jika membuat proker maka semua anggota bem akan diset status prokernya menjadi '1'
	def setProker(self, proker):
		self.__proker.append(proker)
		for anggotas in self.__anggota:
			anggotas.setStatusProker("1")

	def getProker(self):
		return self.__proker

	# method untuk menampilkan list proker beserta statusnya
	def tampilProker(self, karakter):
		i = 0
		print("=== List Proker ===")
		for prokers in self.__proker:
			print(str(i + 1), ". ", prokers, sep='')
			print("   status : ", end="")
			if(karakter.getStatusProker(i) == "1"):
				print("Baru dirancang")
			if(karakter.getStatusProker(i) == "2"):
				print("Sedang dijalankan")
			if(karakter.getStatusProker(i) == "3"):
				print("Sudah selesai")
			i += 1
		print("===================")
		print("")