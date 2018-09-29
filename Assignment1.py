# ********************* Program Angka Terbilang       *********************
# ********************* Nama    : Anindito Bhagawanta *********************
# ********************* NPM     : 1606879230          *********************
# ********************* Kelas   : DDP 1 - B           *********************
# ********************* Asisten : Arie Joseph         *********************

angka = ["", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan"
        , "sembilan", "sepuluh", "sebelas", "dua belas", "tiga belas", 
        "empat belas", "lima Belas", "enam belas", "tujuh belas", "delapan belas",
        "sembilan belas"]
ratus = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
ratus_lagi = ["", "seratus", "dua ratus", "tiga ratus", "empat ratus", "lima ratus", "enam ratus", "tujuh ratus",
              "delapan ratus", "sembilan ratus"]
ribu = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
ribu_lagi = ["", "seribu", "dua ribu", "tiga ribu", "empat ribu", "lima ribu", "enam ribu", "tujuh ribu",
              "delapan Ribu", "sembilan ribu"]
puluh_ribu = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]
puluh_ribu_lagi = ["", "sepuluh ribu", "dua puluh ribu", "tiga puluh ribu", "empat puluh ribu", "lima puluh ribu",
                   "enam puluh ribu" ,"tujuh puluh ribu", "delapan puluh Ribu", "sembilan puluh ribu"] 
belas_ribu = ["", "sebelas ribu", "dua belas ribu", "tiga belas ribu", "empat belas ribu", "lima belas ribu", 
              "enam belas ribu", "tujuh belas ribu", "delapan belas ribu", "sembilan belas ribu"]
belas_ribu_lagi = [0, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000]


while True :
    try:        
        input_angka = int(input("Masukkan bilangan bulat positif dibawah 100000: "))
        break
    except :
       print("Input tidak valid!")
if input_angka < 0:
    print("Input negatif, tidak valid!")
elif input_angka == 0:
    print("Nol")
elif input_angka < 20:
    print(angka[input_angka].capitalize())
elif input_angka < 100:
    print(angka[input_angka // 10].capitalize(), "puluh", angka[input_angka % 10])
elif input_angka % 100 == 0 and input_angka < 1000:
    print(ratus_lagi[input_angka // 100].capitalize())
elif input_angka < 1000:
    if (input_angka // 100) == 1:
        if (input_angka % 100) // 10 == 0:
            print("Seratus", angka[(input_angka - ratus[(input_angka // 100)])])
        elif (input_angka % 100) // 10 == 1:
            print("Seratus", angka[(input_angka - ratus[(input_angka // 100)])])
        else:
            print("Seratus", angka[(input_angka - ratus[(input_angka // 100)]) // 10], "puluh", angka[input_angka % 10])
    elif (input_angka % 100) // 10 == 0:
        print(angka[input_angka // 100].capitalize(), "ratus", angka[(input_angka - ratus[(input_angka // 100)])])
    elif (input_angka % 100) // 10 == 1:
        print(angka[input_angka // 100].capitalize(), "ratus", angka[(input_angka - ratus[(input_angka // 100)])])
    else:
        print(angka[input_angka // 100].capitalize(), "ratus", angka[(input_angka - ratus[(input_angka // 100)]) // 10],
              "puluh", angka[input_angka % 10])
elif input_angka // 1000 == 1 and input_angka < 10000:
    if (input_angka - 1000) < 20:
        print("Seribu", angka[input_angka - 1000])
    elif (input_angka - 1000) < 100:
        print("Seribu", angka[(input_angka - 1000) // 10], "puluh", angka[input_angka % 10])
    elif (input_angka - 1000) < 1000:
        if ((input_angka - 1000) % 100) // 10 == 0:
            print("Seribu", ratus_lagi[(input_angka - 1000) // 100], angka[(input_angka - 1000)% 100])
        elif ((input_angka - 1000) % 100) // 10 == 1:
            print("Seribu", ratus_lagi[(input_angka - 1000) // 100], angka[(input_angka - 1000)% 100])
        else:
            print("Seribu", ratus_lagi[(input_angka - 1000) // 100], angka[((input_angka - 1000)% 100) // 10], "puluh", 
                  angka[input_angka % 10])
elif input_angka < 10000:
    if (input_angka - ribu[input_angka // 1000]) < 20:
        print(angka[input_angka // 1000].capitalize(), "ribu", angka[input_angka % 1000])
    elif (input_angka - ribu[input_angka // 1000]) < 100:
        print(angka[input_angka // 1000].capitalize(), "ribu", angka[(input_angka - ribu[input_angka // 1000]) // 10],
              "puluh", angka[input_angka % 10])
    elif (input_angka - ribu[input_angka // 1000]) < 1000:
        if ((input_angka - ribu[input_angka // 1000]) % 100) // 10 == 0:
            print(angka[input_angka // 1000].capitalize(), "ribu", ratus_lagi[(input_angka - ribu[input_angka // 1000])
            // 100], angka[(input_angka - ribu[input_angka // 1000])% 100])
        elif ((input_angka - ribu[input_angka // 1000]) % 100) // 10 == 1:
            print(angka[input_angka // 1000].capitalize(), "ribu", ratus_lagi[(input_angka - ribu[input_angka // 1000])
            // 100], angka[(input_angka - ribu[input_angka // 1000])% 100])
        else:
            print(angka[input_angka // 1000].capitalize(), "ribu", ratus_lagi[(input_angka - ribu[input_angka // 1000])
            // 100], angka[((input_angka - ribu[input_angka // 1000]) % 100) // 10], "puluh", angka[input_angka 
            % 10])
elif input_angka // 10000 == 1 and input_angka < 100000:
    if (input_angka - 10000) < 20:
        print("Sepuluh ribu", angka[input_angka - 10000])
    elif (input_angka - 10000) < 100:
        print("Sepuluh ribu", angka[(input_angka - 10000) // 10], "puluh", angka[input_angka % 10])
    elif (input_angka - 10000) < 1000:
        if ((input_angka - 10000) % 100) // 10 == 0:
            print("Sepuluh ribu", ratus_lagi[(input_angka - 10000) // 100], angka[(input_angka - 10000)% 100])
        elif ((input_angka - 10000) % 100) // 10 == 1:
            print("Sepuluh ribu", ratus_lagi[(input_angka - 10000) // 100], angka[(input_angka - 10000)% 100])
        else:
            print("Sepuluh ribu", ratus_lagi[(input_angka - 10000) // 100], angka[((input_angka - 10000)% 100) // 10], "puluh", 
                  angka[input_angka % 10])
    elif (input_angka - 10000) // 1000 < 10 and (input_angka - 10000) < 10000:
         if (input_angka - belas_ribu_lagi[(input_angka - 10000) // 1000]) < 20:
            print(belas_ribu[(input_angka - 10000) // 1000].capitalize(), angka[input_angka - belas_ribu_lagi[(input_angka - 10000) // 1000]])
         elif (input_angka - belas_ribu_lagi[(input_angka - 10000) // 1000]) < 100:
            print(belas_ribu[(input_angka - 10000) // 1000].capitalize(), angka[(input_angka - belas_ribu_lagi[(input_angka - 10000) // 1000])//10], 
            "puluh", angka[input_angka % 10])
         elif (input_angka - belas_ribu_lagi[(input_angka - 10000) // 1000]) < 1000:
             if ((input_angka - belas_ribu_lagi[(input_angka - 10000) // 1000]) % 100) // 10 == 0:
                 print(belas_ribu[(input_angka - 10000) // 1000].capitalize(), angka[(input_angka % 1000)//100], "ratus", angka[(input_angka - 
                 belas_ribu_lagi[(input_angka - 10000) // 1000])% 100])
             elif ((input_angka - belas_ribu_lagi[(input_angka - 10000) // 1000]) % 100) // 10 == 1:
                 print(belas_ribu[(input_angka - 10000) // 1000].capitalize(), angka[(input_angka % 1000)//100], "ratus", angka[(input_angka - 
                 belas_ribu_lagi[(input_angka - 10000) // 1000])% 100])
             else:
                 print(belas_ribu[(input_angka - 10000) // 1000].capitalize(), angka[(input_angka % 1000)//100], "ratus", angka[((input_angka - 
                 belas_ribu_lagi[(input_angka - 10000) // 1000])% 100) // 10], "puluh",  angka[input_angka % 10])
elif input_angka < 100000:
    if (input_angka - puluh_ribu[input_angka // 10000]) < 20:
        print(puluh_ribu_lagi[input_angka // 10000].capitalize(), angka[input_angka % 1000])
    elif (input_angka - puluh_ribu[input_angka // 10000]) < 100:
        print(puluh_ribu_lagi[input_angka // 10000].capitalize(), angka[(input_angka % 1000) // 10], "puluh", angka[input_angka % 10])
    elif (input_angka - puluh_ribu[input_angka // 10000]) < 10000:
        if ((input_angka - puluh_ribu[input_angka // 10000]) % 100) // 10 == 0:
            print(puluh_ribu_lagi[input_angka // 10000].capitalize(), ratus_lagi[(input_angka%1000)//100], angka[input_angka % 100])
        elif ((input_angka - puluh_ribu[input_angka // 10000]) % 100) // 10 == 1:
            print(puluh_ribu_lagi[input_angka // 10000].capitalize(), ratus_lagi[(input_angka%1000)//100], angka[input_angka % 100])
        else:
            print(puluh_ribu_lagi[input_angka // 10000].capitalize(), ratus_lagi[(input_angka%1000)//100], angka[(input_angka % 100)//10], "puluh", angka[input_angka % 10])
elif input_angka == 100000:
    print("Seratus ribu")
elif input_angka > 100000:
    print("Input diluar jangkauan, tidak valid!")