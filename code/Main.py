# Saya Mochamad Khaairi NIM 2106416 mengerjakan TP1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. Aamiin.

# import dari class lain
from Mahasiswa import Mahasiswa
from Dosen import Dosen
from Prodi import Prodi
from Asprak import Asprak
from BEM import BEM
from AnggotaBEM import AnggotaBEM
from EngClub import EngClub
from AnggotaEngClub import AnggotaEngClub
from Pilihan import Pilihan
from Matkul import Matkul

# instansiasi class Matkul
matkul1 = Matkul("Struktur Data")
matkul2 = Matkul("Kecerdasan Buatan")
matkul3 = Matkul("Data Mining")

# instansiasi mahasiswa (yaitu dari class Mahasiswa, AnggotaBEM, anggotaEngClub dan Asprak)
resyad = Mahasiswa("189001", "Resyad", "Laki-Laki", 20, "210716", "UPI", "FPMIPA", "Ilmu Komputer", "Origin", "Asus", "Mahasiswa Biasa")
pahri = AnggotaBEM("107811", "Pahri", "Laki-Laki", 18, "210717", "UPI", "FPMIPA", "Ilmu Komputer", "Jalan Yang Jauh Jangan Lupa Pulang", "Acer", "Anggota BEM", "Ketua")
angga = AnggotaEngClub("189167", "Angga", "Laki-Laki", 20, "210851", "UPI", "FPMIPA", "Ilmu Komputer", "Raja Ratu & Rahasia", "VivoBook", "Anggota EngClub", "Ketua", "510")
getsbi = AnggotaEngClub("158910", "Getsbi", "Laki-Laki", 19, "219910", "UPI", "FPMIPA", "Ilmu Komputer", "I'm Thinking Of Ending Things", "VivoBook", "Anggota EngClub", "Anggota", "501")
mila = Asprak("130167", "Mila", "Perempuan", 20, "219812", "UPI", "FPMIPA", "Ilmu Komputer", "Angels & Demons", "Asus", "Asisten Praktikum", "Struktur Data")
# instansiasi class Dosen
rose = Dosen("110719", "Mrs. Rose", "Perempuan", 36, "118912", "Struktur Data", "Freeman", "Asus", "Dosen")

# instansiasi class Prodi
prodi = Prodi(resyad, rose, matkul1, "Ilmu Komputer", "IK")
prodi.setMahasiswa(pahri)
prodi.setMahasiswa(angga)
prodi.setMahasiswa(getsbi)
prodi.setMahasiswa(mila)
prodi.setMatkul(matkul2)
prodi.setMatkul(matkul3)

# instansiasi organisasi, yaitu BEM dan EngClub
bem = BEM(pahri, "Pahri")
engclub = EngClub(angga, "Angga")
engclub.setAnggota(getsbi)

# instansiasi untuk class Pilihan yang berisi pilihan menu
pilih = Pilihan()

n = 0
m = 0
flag1 = True
flag2 = True

# perulangan untuk pilihan menu
while flag1:
	print("==========================================")
	print("1. Tampilkan data prodi\n2. Pilih karakter\n3. Keluar\nMasukkan menu : ", end="")
	# inputan untuk pilihan
	n = int(input())
	print("==========================================")
	# jika pilihannya 1 maka tampilkan data prodi
	if(n == 1):
		prodi.tampil()
	# jika pilihannya 2 maka pilih untuk karakter
	if(n == 2):
		while flag2:
			print("1. Resyad\n2. Pahri\n3. Angga\n4. Getsbi\n5. Mila\n6. Mrs Rose\n7. Batal\nMasukkan karakter yang akan dipilih : ", end="")
			m = int(input())
			if(m == 1):
				pilih.pilih(resyad, bem, prodi, engclub)
			if(m == 2):
				pilih.pilih(pahri, bem, prodi, engclub)
			if(m == 3):
				pilih.pilih(angga, bem, prodi, engclub)
			if(m == 4):
				pilih.pilih(getsbi, bem, prodi, engclub)
			if(m == 5):
				pilih.pilih(mila, bem, prodi, engclub)
			if(m == 6):
				pilih.pilih(rose, bem, prodi, engclub)
			if(m == 7):
				flag2 = False
	flag2 = True
	# jika 3 maka keluar
	if(n == 3):
		flag1 = False