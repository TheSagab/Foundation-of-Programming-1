# ********************* Program Buku Penilaian        *********************
# ********************* Nama    : Anindito Bhagawanta *********************
# ********************* NPM     : 1606879230          *********************
# ********************* Kelas   : DDP 1 - B           *********************
# ********************* Asisten : Arie Joseph         *********************

Database = {}


def ASCIIArt():
    print(" _______ _           _____                   _     ")
    print("|__   __| |         / ____|                 | |    ")
    print("   | |  | |__   ___| (___   __ _  __ _  __ _| |__  ")
    print("   | |  | '_ \ / _ \\\\___ \ / _` |/ _` |/ _` | '_ \ ")
    print("   | |  | | | |  __/____) | (_| | (_| | (_| | |_) |")
    print("   |_|  |_| |_|\___|_____/ \__,_|\__, |\__,_|_.__/ ")
    print("                                  __/ |            ")
    print("                                 |___/             ")


def Add(Mahasiswa, Kelas):								 			# Menambah mahasiswa ke Database
    if Mahasiswa in Database:										# Jika sudah terdapat di Database
        print("Mahasiswa {} sudah ada di dalam buku.".format(Mahasiswa))
    else:
        DafKelas = ["A", "B", "C", "D"]
        if Kelas.upper() not in DafKelas:								# Daftar kelas yang valid adalah A, B, C dan D
            print("Kelas yang valid adalah A, B, C dan D!")
        else:
            # Memasukkan mahasiswa ke Database dan assign data kelas,
            Database[Mahasiswa] = [Kelas.upper(), [0, 0], [0, 0, 0], [0, 0]]
            # quiz, tugas, dan ujian ke Database (default nilai 0)
            print(Mahasiswa + " berhasil ditambahkan kedalam buku.")


def Update(Mahasiswa, Berkas, Nilai):								# Mengupdate berkas nilai mahasiswa
    Nilainya = Nilai.split(",")
    if Berkas == "Quiz":											# Mengupdate sesuai berkas yang dinilai
        # Index 1, 2, 3 masing-masing Quiz, Tugas dan Ujian
        for i in range(len(Nilainya)):
            # Jika nilai kosong (""), maka dilewati dan dianggap tetap 0
            if Nilainya[i] == "":
                continue											# Melakukan iterasi sebanyak i kali, dengan i = banyak nilai yang diinput
            else:													# Setiap iterasi menggantikan nilai pada index tersebut dengan nilai
                Database[Mahasiswa][1][i] = int(Nilainya[i])		# yang diinginkan
    elif Berkas == "Tugas":
        for i in range(len(Nilainya)):
            if Nilainya[i] == "":
                continue
            else:
                Database[Mahasiswa][2][i] = int(Nilainya[i])
    elif Berkas == "Ujian":
        for i in range(len(Nilainya)):
            if Nilainya[i] == "":
                continue
            else:
                Database[Mahasiswa][3][i] = int(Nilainya[i])
    print("Menambah nilai {} pada mahasiswa {}.".format(Berkas, Mahasiswa))


def Average(Kelas, Berkas, Ke):										# Menghitung Rata-rata berkas tertentu dari suatu kelas
    Jumlah = 0														# Menginisiasi Jumlah dan Count di 0
    count = 0														# Jumlah bertambah pada saat mengakses Database dan mencari nilai
    for i in Database:												# di kelas dan berkas tertentu
        # count bertambah ketika berhasil menambahkan Jumlah, dan count
        for j in range(len(Database)):
            if Database[i][0] == Kelas:								# menunjukkan jumlah mahasiswa di kelas tersebut
                if Berkas == "Quiz":								# RataRata dihitung dengan hasil bagi Jumlah dan count
                    # i adalah Mahasiswa, dan j adalah banyak Mahasiswa di
                    # Database
                    Jumlah += Database[i][1][int(Ke) - 1]
                    count += 1										# round() digunakan untuk membulatkan hingga 2 angka dibelakang koma
                elif Berkas == "Tugas":
                    Jumlah += Database[i][2][int(Ke) - 1]
                    count += 1
                elif Berkas == "Ujian":
                    Jumlah += Database[i][3][int(Ke) - 1]
                    count += 1
    RataRata = CekInt(round((Jumlah / count), 2))
    print("Rata-rata nilai {} {} pada kelas {} adalah {}.".format(Berkas,
                                                                  Ke, Kelas, str(RataRata).replace(".", ",")))


def Summary(Mahasiswa):													# Mencetak rekap nilai suatu mahasiswa
    # Menghitung rata-rata nilai quiz, tugas dan ujian dan nilai akhirnya
    AverageQuiz = CekInt(round((sum(Database[Mahasiswa][1]) / 2), 2))
    # dan kemudian mencetaknya
    AverageTugas = CekInt(round((sum(Database[Mahasiswa][2]) / 3), 2))
    AverageUjian = CekInt(round((sum(Database[Mahasiswa][3]) / 2), 2))
    NilaiAkhir = CekInt(
        round((0.2 * AverageTugas + 0.3 * AverageQuiz + 0.5 * AverageUjian), 2))
    print("Nama        : " + Mahasiswa)
    print("Kelas       : " + Database[Mahasiswa][0])
    # .replace(".", ",") digunakan untuk mengubah titik menjadi koma
    print("Quiz        : {}".format(str(AverageQuiz).replace(".", ",")))
    print("Tugas       : {}".format(str(AverageTugas).replace(".", ",")))
    print("Ujian       : {}".format(str(AverageUjian).replace(".", ",")))
    print("Nilai Akhir : {}".format(str(NilaiAkhir).replace(".", ",")))


def Search(Berkas, Ke, Nilai):										# Mencari berkas nilai mahasiswa dengan nilai tertentu
    # Nilainya[0] adalah batas bawah dan Nilainya[1] adalah batas atas
    Nilainya = Nilai.split("-")
    # Jika Nilainya[0] <= Nilai <= Nilainya[1] maka akan mencetak mahasiswa
    # yang memiliki nilai tersebut pada berkas tertentu
    for i in Database:
        if Berkas == "Quiz":										# i adalah Mahasiswa
            if Database[i][1][int(Ke) - 1] >= int(Nilainya[0]) and Database[i][1][int(Ke) - 1] <= int(Nilainya[1]):
                print(i)
        elif Berkas == "Tugas":
            if Database[i][2][int(Ke) - 1] >= int(Nilainya[0]) and Database[i][1][int(Ke) - 1] <= int(Nilainya[1]):
                print(i)
        elif Berkas == "Ujian":
            if Database[i][3][int(Ke) - 1] >= int(Nilainya[0]) and Database[i][1][int(Ke) - 1] <= int(Nilainya[1]):
                print(i)


def CekInt(x):													# Mengecek apakah bilangan bulat
    if x.is_integer():											# Jika tidak ada angka dibelakang koma, maka
        return int(x)											# mengembalikan bilangan bulat
    else:
        return x


def Main():																				# Penggunaan .lower().captialize dan .upper() agar tidak case-sensitive
    while True:																			# Program berjalan sampai tak hingga
        try:
            # Cek apakah input berkas sesuai
            BerkasValid = ["Quiz", "Tugas", "Ujian"]
            # Memisahkan menjadi list [Command, Parameter Command]
            masukkan = input().split()
            if masukkan[0].upper() == "ADD":
                # Memisahkan menjadi list [Mahasiswa, Kelas]
                Parameter = masukkan[1].split(";")
                Add(Parameter[0].lower().capitalize(),
                    Parameter[1]) 					# Mahasiswa, Kelas
            elif masukkan[0].upper() == "UPDATE":
                # Memisahkan menjadi list [Mahasiswa, Berkas, Nilai (masih
                # belum terpisah koma)]
                Parameter = masukkan[1].split(";")
                if Parameter[1] not in BerkasValid:
                    print("Input berkas tidak valid!")
                else:
                    Update(Parameter[0].lower().capitalize(), Parameter[
                           1], Parameter[2]) 	# Mahasiswa, Berkas, Nilai
            elif masukkan[0].upper() == "AVERAGE":
                # Memisahkan menjadi list [Kelas, Berkas, Berkas keberapa]
                Parameter = masukkan[1].split(";")
                if Parameter[1] not in BerkasValid:
                    print("Input berkas tidak valid!")
                else:
                    # Kelas, Berkas, Ke
                    Average(Parameter[0], Parameter[1], Parameter[2])
            elif masukkan[0].upper() == "SUMMARY":
                Summary(masukkan[1].lower().capitalize())								# Mahasiswa
            elif masukkan[0].upper() == "SEARCH":
                # Memisahkan menjadi list [Berkas, Berkas keberapa, Nilai
                # (masih belum terpisah strip)]
                Parameter = masukkan[1].split(";")
                if Parameter[0] not in BerkasValid:
                    print("Input berkas tidak valid!")
                else:
                    # Berkas, Ke, Nilai
                    Search(Parameter[0], Parameter[1], Parameter[2])
            else:
                print("Input tidak valid!")
        except IndexError:																# Jika memasukkan nilai diluar jangkauan
            print("Input tidak valid / diluar jangkauan!")
        except KeyError:																# Jika memanggil suatu perintah tetapi belum ada mahasiswa tersebut
            print("Mahasiswa belum terdaftar di buku!")
        except EOFError:																# Jika mencapai End-of-file
            break
        except ValueError:																# Jika nilai terdapat huruf
            print("Nilai mengandung karakter non angka!")
        except KeyboardInterrupt:														# Jika menekan Ctrl-C
            print("Ctrl-C ditekan, menghentikan program.")
            break
        # print(Database)																# Untuk debugging

ASCIIArt()
Main()																					# Eksekusi Program
