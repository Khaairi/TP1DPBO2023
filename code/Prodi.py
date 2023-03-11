# Saya Mochamad Khaairi NIM 2106416 mengerjakan TP1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. Aamiin.

# inisialisasi class Prodi
class Prodi:
	__namaProdi = ""
	__kode = ""
	__mahasiswa = []
	__dosen = []
	__matkul = []

	# constructor
	# untuk mahasiswa dan dosen akan diinput dengan object, composite dari class Mahasiswa, class Dosen dan class Course
	def __init__(self, mahasiswa, dosen, matkul, namaProdi = "", kode = ""):
		self.__namaProdi = namaProdi
		self.__kode = kode
		# karena berbentuk list, maka diinputnya menggunakan append
		# nantinya list akan berisi kumpulan object
		self.__mahasiswa.append(mahasiswa)
		self.__dosen.append(dosen)
		self.__matkul.append(matkul)

	# kumpulan method setter dan getter untuk tiap atribut
	def setNamaProdi(self, namaProdi):
		self.__namaProdi = namaProdi

	def getNamaProdi(self):
		return self.__namaProdi

	def setKode(self, kode):
		self.__kode = kode

	def getKode(self):
		return self.__kode

	def setMahasiswa(self, mahasiswa):
		self.__mahasiswa.append(mahasiswa)

	def getMahasiswa(self):
		return self.__mahasiswa

	def setDosen(self, dosen):
		self.__dosen.append(dosen)

	def getDosen(self):
		return self.__dosen

	def setMatkul(self, matkul):
		self.__matkul.append(matkul)

	def getMatkul(self):
		return self.__matkul

	# method untuk menampilkan data prodi
	def tampil(self):
		print("=== Program Studi", self.__namaProdi, "===")
		print("Kode Program Studi :", self.__kode)
		i = 0
		print("\nList Mahasiswa :")
		for mahasiswas in self.__mahasiswa:
			print(str(i + 1), ". ", mahasiswas.getName(), sep='')
			i += 1
		i = 0
		print("\nList Dosen :")
		for dosens in self.__dosen:
			print(str(i + 1), ". ", dosens.getName(), sep='')
			i += 1
		i = 0
		print("\nList Mata Kuliah :")
		for matkuls in self.__matkul:
			print(str(i + 1), ". ", matkuls.getNamaMatkul(), sep='')
			i += 1