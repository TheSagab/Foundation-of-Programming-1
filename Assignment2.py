# ********************* Program Angka Terbilang 2     *********************
# ********************* Nama    : Anindito Bhagawanta *********************
# ********************* NPM     : 1606879230          *********************
# ********************* Kelas   : DDP 1 - B           *********************
# ********************* Asisten : Arie Joseph         *********************

def AngkaTerbilang(bil):
    angka=["","satu","dua","tiga","empat","lima","enam","tujuh","delapan","sembilan","sepuluh","sebelas"]
    Hasil =" "
    n = int(bil)
    if n == 0:
        Hasil = "nol"
    elif n > 0 and n <= 11:
    	  Hasil += angka[n] #angka 1 - 11
    elif n < 20:
    	  Hasil = AngkaTerbilang(n % 10) + " belas" #angka 12-20
    elif n < 100:
    	  Hasil = AngkaTerbilang(n / 10) + " puluh" + AngkaTerbilang(n % 10) #angka 21-99
    elif n < 200:
    	  Hasil = " seratus" + AngkaTerbilang(n - 100) #angka 100-199
    elif n < 1000:
    	  Hasil = AngkaTerbilang(n / 100) + " ratus" + AngkaTerbilang(n % 100) #angka 200-999
    elif n < 2000:
    	  Hasil = " seribu" + AngkaTerbilang(n - 1000) #angka 1000-1999
    elif n < 1000000:
    	  Hasil = AngkaTerbilang(n / 1000) + " ribu" + AngkaTerbilang(n % 1000) #angka 2000-999999
    elif n < 1000000000:
        Hasil = AngkaTerbilang(n / 1000000) + " juta" + AngkaTerbilang(n % 1000000) #angka 1000000-99999999
    else:
        Hasil = AngkaTerbilang(n / 1000000000) + " milyar" + AngkaTerbilang(n % 100000000) #angka 1000000000-99999999999
    return Hasil
     
def AngkaBelakangKoma(kata):
    desimal = ["nol", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan"
        , "sembilan"]
    Hasil = " "
    for i in kata:
        Hasil += desimal[int(i)] + " " # menghasilkan kata desimal setiap iterasi kata
    return Hasil

def AngkaKoma(x,y):
    return AngkaTerbilang(x) + " koma " + AngkaBelakangKoma(y) # angka terbilang koma angka belakang koma

print("Starting program...")
while True:
    try:
        FileIn = open("input_text.txt", "r") #mencoba membuka file, jika ada maka keluar dari loop
        break
    except:
        print("File tidak ditemukan! Program akan ditutup.")
        raise SystemExit #jika tidak ditemukan file program ditutup

lstKata = FileIn.readlines() # mengubah file string di text menjadi list
HasilKata = ""
for i in range(len(lstKata)): # iterasi indeks sebanyak jumlah list kata 
    katanya = lstKata[i].split(" ") # memisahkan list kata 
    for j in range(len(katanya)): # iterasi indeks sebanyak kata
        if katanya[j].isnumeric(): # jika kata tersebut mengandung hanya angka
            katanya[j] = AngkaTerbilang(katanya[j]) # mengubah string tersebut menjadi angka terbilang
        elif "," in katanya[j]: #jika kata tersebut mengandung koma
            try:
                float(i) # memastikan mengambil angka dengan komanya
                koma = katanya[j].split(",") # memisahkan depan koma dengan belakang koma
                katanya[j] = AngkaKoma(koma[0], koma[1]) # depan koma diubah menjadi angka terbilang, sedangkan belakang koma diubah menjadi angka belakang koma
            except:
                continue # jika kata tersebut mengandung koma tetapi tidak ada angka, maka kata dilewati
        else:
            continue # melanjutkan string biasa
    HasilKata += " ".join(katanya) # menggabungkan hasil dari sebelumnya
FileOut = open("output_text.txt", "w")
FileOut.write(HasilKata) # menulis hasil kata ke output_text.txt
FileIn.close()
FileOut.close()
print("Program done!")
