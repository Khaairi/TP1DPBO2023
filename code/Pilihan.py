# Saya Mochamad Khaairi NIM 2106416 mengerjakan TP1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. Aamiin.

# inisialisasi class Pilihan
class Pilihan:
	# constructor
	def __init__(self):
		pass

	# method yang berisi opsi pilihan (semacam menu pilihan) untuk tiap karakternya
	def pilih(self, karakter, bem, prodi, EngClub):
		flag = True
		n = 0
		while flag:
			if(karakter.getStatus() == "Mahasiswa Biasa"):
				print("(1)Tampilkan data diri dan nilai (2)Makan (3)Minum (4)Tidur (5)Beli buku baru\n(6)Beli laptop baru (7)Belajar (8)Kontrak Matkul (9)Tampilkan List Tugas (10)Batal\nMasukkan kegiatan : ", end="")
				n = int(input())
			if(karakter.getStatus() == "Asisten Praktikum"):
				print("(1)Tampilkan data diri dan nilai (2)Makan (3)Minum (4)Tidur (5)Beli buku baru (6)Beli laptop baru\n(7)Belajar (8)Kontrak Matkul (9)Tampilkan List Tugas (10)Mengajar (11)Beri tugas praktikum (12)Beri nilai praktikum (13)Batal\nMasukkan kegiatan : ", end="")
				n = int(input())
			if(karakter.getStatus() == "Anggota BEM"):
				print("(1)Tampilkan data diri dan nilai (2)Makan (3)Minum (4)Tidur (5)Beli buku baru (6)Beli laptop baru (7)Belajar\n(8)Kontrak Matkul (9)Tampilkan List Tugas (10)Tampilkan list proker  (11)Rancang proker (12)Jalankan proker (13)Hadiri evaluasi proker (14)Batal\nMasukkan kegiatan : ", end="")
				n = int(input())
			if(karakter.getStatus() == "Anggota EngClub"):
				print("(1)Tampilkan data diri dan nilai (2)Makan (3)Minum (4)Tidur (5)Beli buku baru (6)Beli laptop baru\n(7)Belajar (8)Kontrak Matkul (9)Tampilkan List Tugas (10)Practicing English (11)rancangan proker (12)Batal\nMasukkan kegiatan : ", end="")
				n = int(input())
			if(karakter.getStatus() == "Dosen"):
				print("(1)Tampilkan data diri (2)Makan (3)Minum (4)Tidur (5)Beli spidol baru\n(6)Beli laptop baru (7)Mengajar (8)Beri nilai (9)Batal\nMasukkan kegiatan : ", end="")
				n = int(input())

			if(n == 1):
				karakter.tampil(karakter)
			if(n == 2):
				karakter.eat()
			if(n == 3):
				karakter.drink()
			if(n == 4):
				karakter.sleep()
			if(karakter.getStatus() != "Dosen"):
				if(n == 5):
					print("Masukkan nama buku : ", end="")
					buku = str(input())
					karakter.setBooks(buku)
			if(karakter.getStatus() == "Dosen"):
				if(n == 5):
					print("Masukkan merk spidol : ", end="")
					spidol = str(input())
					karakter.setMarkers(spidol)
				if(n == 7):
					karakter.mengajar(karakter)
				if(n == 8):
					karakter.beriNilai(prodi)
				if(n == 9):
					flag = False
			if(n == 6):
				print("Masukkan nama laptop : ", end="")
				laptop = str(input())
				karakter.setLaptops(laptop)
			if(karakter.getStatus() != "Dosen"):	
				if(n == 7):
					karakter.study(karakter)
				if(n == 8):
					tanda = 0
					print("Masukkan nama mata kuliah : ", end="")
					namaMatkul = str(input())
					for matkul in prodi.getMatkul():
						if(matkul.getNamaMatkul() == namaMatkul):
							karakter.setMatkul(namaMatkul)
							tanda = 1
							print("Berhasil mengontrak mata kuliah!\n")
					if(tanda == 0):
						print("Mata kuliah tidak tersedia\n")
				if(n == 9):
					karakter.tampilTugas()
			if(karakter.getStatus() == "Mahasiswa Biasa"):
				if(n == 10):
					flag = False
			if(karakter.getStatus() == "Asisten Praktikum"):
				if(n == 10):
					karakter.mengajar(karakter)
				if(n == 11):
					karakter.beriTugas(karakter, prodi)
				if(n == 12):
					karakter.beriNilai(prodi)
				if(n == 13):
					flag = False
			if(karakter.getStatus() == "Anggota BEM"):
				if(n == 10):
					bem.tampilProker(karakter)
				if(n == 11):
					karakter.rancangProker(bem)
				if(n == 12):
					karakter.jalankanProker(bem)
				if(n == 13):
					karakter.hadiriEvaluasi(bem)
				if(n == 14):
					flag = False
			if(karakter.getStatus() == "Anggota EngClub"):
				if(n == 10):
					karakter.belajarEng(karakter)
				if(n == 11):
					karakter.rancangProker(EngClub)
				if(n == 12):
					flag = False

		print("=============================")
