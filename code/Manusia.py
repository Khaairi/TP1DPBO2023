# Saya Mochamad Khaairi NIM 2106416 mengerjakan TP1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. Aamiin.

# inisialisasi class Manusia
class Manusia:
	# atribut
	__nik = ""
	__name = ""
	__gender = ""
	__age = 0

	# constructor
	def __init__(self, nik = "", name = "", gender = "", age = 0):
		self.__nik = nik
		self.__name = name
		self.__gender = gender
		self.__age = age

	# method setter dan getter
	def setNik(self, nik):
		self.__nik = nik

	def getNik(self):
		return self.__nik

	def setName(self, name):
		self.__name = name

	def getName(self):
		return self.__name

	def setGender(self, gender):
		self.__gender = gender

	def getGender(self):
		return self.__gender

	def setAge(self, age):
		self.__age = age

	def getAge(self):
		return self.__age

	# method dari kegiatan-kegiatan manusia pada umumnya
	def eat(self):
		print(self.__name, "is eating\n")

	def drink(self):
		print(self.__name, "is drinking\n")

	def sleep(self):
		print(self.__name, "is sleeping\n")