# TP1DPBO2023
Saya Mochamad Khaairi NIM 2106416 mengerjakan TP1 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

## Desain Program
![desaign2 drawio](https://user-images.githubusercontent.com/100757455/224470614-84414b10-ff2d-49d9-b344-6d4e30fb3d99.png)

Program didesain menjadi sepuluh class
* **Manusia**
* **Mahasiswa**
* **Asprak**
* **AnggotaBEM**
* **AnggotaEngClub**
* **Dosen**
* **BEM**
* **EngClub**
* **Prodi**
* **Matkul**

Penjelasan Relasi:
class `Manusia` memiliki child yaitu class `Mahasiswa` dan `Dosen` karena merupakan object yang sama, lalu class `Mahasiswa` memiliki child juga yaitu class `Asprak`, `AnggotaBEM` dan `AnggotaEngclub` karena merupakan object yang sama yaitu mahasiswa. Lalu pada class `Prodi` terdapat list dari mahasiswa, dosen dan matkul yang mana merupakan composite dari ketiga kelas tersebut (jadi isi dari listnya adalah object), pada class `Mahasiswa` men-composite class `Matkul` karena tiap mahasiswa memliki mata kuliah yang dikontrak. Pada class `Asprak` composite class `Mahasiwa` karena asisten praktikum memiliki mahasiswa yang dia ajar begitu juga pada class `Dosen`. Lalu pada class `BEM` dan `EngClub` masing-masing men-composite class anggotanya, jadi pada class `BEM` dan `EngClub` terdapat list anggota yang berisi object.

Pada class `Manusia` terdapat empat atribut:
* **nik**    -> berisi NIK mahasiswa, `string`
* **name**   -> berisi nama mahasiswa, `string`
* **gender** -> berisi jenis kelamin mahasiswa, `string`
* **age** -> berisi usia mahasiswa, `string`\
Terdapat method setter dan getter serta method `eat`, `sleep` dan `drink` (isinya hanya print biasa)

Pada class `Mahasiswa` berisi semua atribut dan method dari class `Manusia` sebagai parent classnya beserta tambahan sembilan atribut:
* **nim** -> berisi NIM mahasiswa, `string`
* **univ** -> berisi nama universitas, `string`
* **faculty** -> berisi nama fakultas, `string`
* **major** -> berisi nama program studi, `string`
* **books** -> berisi kumpulan nama buku, `list string`
* **laptops** -> berisi kumpulan nama laptop, `list string`
* **status** -> berisi status mahasiswa, apakah mahasiswa biasa atau yang lainnya, `string`
* **tugasPrak** -> berisi kumpulan nama tugas praktikum, `list string`
* **matkul** -> berisi kumpulan mata kuliah yang dikontrak, `list object Mahasiswa`\
Terdapat method `tampil` untuk menampilkan data mahasiswa dan method `tampilTugas` untuk menampilkan list tugas praktikum

Pada class `Asprak` berisi semua atribut dan method dari class `Mahasiswa` sebagai parent classnya beserta tambahan satu atribut:
* **namaPrak** -> nama praktikum yang diajarkan, `string`\
Terdapat method `mengajar` yang berisi print biasa, method `beriNilai` untuk memberikan nilai kepada salah satu mahasiswa dan method `beriTugas` untuk memberikan tugas praktikum ke semua mahasiswa

Pada class `AnggotaBEM` berisi semua atribut dan method dari class `Mahasiswa` sebagai parent classnya berserta tambahan dua atribut:
* **jabatan** -> berisi jabatan dari anggotanya, `string`
* **statusProker** -> berisi kumpulan status dari tiap proker, `list string`\
Terdapat method `rancangProker`, `jalankanProker` dan `hadiriEvaluasi` jadi anggotanya dapat merancang, menjalankan dan menghadiri evaluasi untuk prokernya. Pada method `hadiriEvaluasi` terdapat batasan yaitu proker harus dijalankan terlebih dahulu

Pada class `AnggotaEngClub` berisi semua atribut dan method dari class `Mahasiswa` sebagai parent classnya berserta tambahan dua atribut:
* **jabatan** -> berisi jabatan dari anggotanya, `string`
* **scoreTOEFL** -> berisi score toefl dari mahasiswa, `string`\
Terdapat method `belajarEng` dan `rancangProker`

Pada class `Dosen` berisi semua atribut dan method dari class `Manusia` sebagai parent classnya beserta tambahan lima atribut:
* **nip** -> berisi NIP dosen, `string`
* **mastery** -> berisi keahlian dosen, `string`
* **markers** -> berisi kumpulan nama spidol yang dimiliki dosen, `list string`
* **laptops** -> berisi kumpulan nama laptop yang dimiliki dosen, `list string`
* **status** -> berisi status (yaitu dosen), `string`\
Terdapat method `tampil` untuk menampilkan data diri dosen, method `mengajar` dan method `beriNilai` untuk memberikan nilai kepada salah satu mahasiswa. Terdapat batasan bahwa dosen hanya dapat memberi nilai kepada mahasiswa yang nilai praktikumnya sudah terisi

Pada class `BEM` terdapat tiga atribut:
* **ketua** -> berisi nama ketua BEM, `string`
* **proker** -> berisi kumpulan nama proker, `list string`
* **anggota** -> berisi kumpulan object anggota bem, `list object AnggotaBEM`\
Terdapat method `tampilProker` untuk menampilkan semua proker yang ada

Pada class `EngClub` terdapat tiga atribut:
* **ketua** -> berisi nama ketua engclub, `string`
* **anggota** -> berisi kumpulan object anggota engclub, `list object AnggotaEngClub`\
Terdapat method setter dan getter

Pada class `Prodi` terdapat lima atribut:
* **namaProdi** -> berisi nama program studi, `string`
* **kode** -> berisi kode program studi, `string`
* **mahasiswa** -> berisi kumpulan mahasiswa yang terdapat di prodi, `list object Mahasiswa`
* **dosen** -> berisi kumpulan dosen yang terdapat di prodi, `list object Dosen`
* **matkul** -> berisi kumpulan mata kuliah yang terdapat di prodi, `list object Matkul`\
Terdapat method `tampil` untuk menampilkan data prodi

Pada class `Matkul`terdapat tiga atribut:
* **namaMatkul** -> berisi nama mata kuliah, `string`
* **nilaiMatkul** -> berisi nilai dari mata kuliah tersebut, `int`
* **nilaiPrak** -> berisi nilai praktikum dari mata kuliah tersebut, `int`\
Terdapat method setter dan getter

## Alur Program
Alur program ditentukan dari inputan user, program akan menampilkan menu pilihan yang dapat dipilih oleh user, pada pilihan pertama yaitu pilihan untuk menampilkan data prodi atau memilih karakter, jika user memilih karakter maka akan ditampilkan lagi pilihan untuk memilih karakter (ada Resyad, Pahri, Angga, Getsbi, Mila dan Mrs Rose), tiap karakter memiliki rolenya masing-masing yang mana jika dipilih akan menampilkan tampilan pilihannya masing masing, misalkan Pahri yang seorang anggota BEM maka terdapat pilihan untuk merancang proker berbeda dengan Resyad yang hanya mahasiswa biasa, lalu Mrs Rose yang merupakan seorang dosen yang terdapat pilihan untuk memberikan nilai kepada mahasiswa.

Pada pilihan rancang proker, jalankan proker dan hadiri evaluasi user diminta untuk menginput nama prokernya. Pada pilihan memberi nilai baik dari asprak atau dosen, user diminta untuk menginput nama mahasiwa lalu nama mata kuliahnya dan terakhir nilainya. Untuk tiap pilihan terdapat error handlingnya masing masing.

## Dokumentasi

![Screenshot (1)](https://user-images.githubusercontent.com/100757455/224475091-63191488-913e-4407-aa82-7d033939fda0.png)
![Screenshot (2)](https://user-images.githubusercontent.com/100757455/224475094-be8c0922-2ca8-4f85-ba79-48f25036028e.png)
![Screenshot (3)](https://user-images.githubusercontent.com/100757455/224475099-edcbfce1-598d-49c2-99cd-d1deadae12c8.png)
![Screenshot (4)](https://user-images.githubusercontent.com/100757455/224475116-10df945a-9faf-445f-bef3-7fbd8efb18c3.png)
