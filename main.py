#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#this is my first project 

#import module
import os, math, platform
from datetime import datetime

#clear terminal's screen
if platform.system().lower() == 'windows':
    os.system('cls')
else:
    os.system('clear')

today = datetime.now().strftime("%d, %B %Y") #date of today, format(dd, mm, yyyy: 1 Jan 2020)

#banner
print(f"""
     --------------------------------
    ||                              ||
    ||   WELCOME TO MY PROGRAM      ||
    ||    By: Khairul Saputra       ||
    ||                              ||
     --------------------------------
            {today}
    1.Persegi               6.Balok
    2.Persegi panjang       7.Bola
    3.Jajar Genjang         8.ukuran pusat, variasi, posisi data
    4.Segitiga              9.permutasi dan kombinasi
    5.lingkaran             10.exit
    """)


#fungsi rumus persegi
def persegi():
    try:
        sisi = int(input("Masukan sisi persegi: "))
        luas = sisi**2
        keliling = 4 * sisi
        print(f"luas persegi: {luas}")
        print(f"keliling persegi: {keliling}")
    except ValueError:
        print("Masukan angka yang valid!")
        print("Ctrl + c untuk keluar")
        

#fungsi rumus persegiPanjang
def persegiPanjang():
    try:
        panjang = int(input("Masukan panjang persegi panjang: "))
        lebar = int(input("Masukan lebar persegi panjang: "))
        luasPersegi = panjang * lebar
        kelilingPersegi = 2 * (panjang + lebar)
        print(f"luas persegi panjang: {luasPersegi}")
        print(f"keliling persegi panjang :{kelilingPersegi}")
    except ValueError:
        print("Masukan angka yang valid")


#fungsi rumus jajarGenjang
def jajarGenjang():
    try:
        alas = int(input("Masukan alas: "))
        sisiMiring = int(input("Masukan sisi miring: "))
        tinggi = int(input("Masukan tinggi jajar genjang: "))
        luas = alas * tinggi
        keliling = 2 * (alas + sisiMiring)
        print(f"Luas jajar Genjang: {luas}")
        print(f"Keliling jajar genjang adalah: {keliling}")
    except ValueError:
        print("Masukan angka yang valid")


#fungsi rumus segitiga
def segitiga():
    try:
        user = int(input("1.Segitiga sama kaki\n2.Segitiga siku-siku\nMasukan pilihan anda: "))
        if user == 1:
            sisi = int(input("Masukan sisi segitiga sama kaki: "))
            tinggi = int(input("Masukan tinggi segitiga sama kaki: "))
            alas = int(input("Masukan alas segitiga sama kaki :"))
            luas = 0.5 * alas * tinggi
            keliling = (2 * sisi) + alas
            print(f"Luas segitiga sama kaki :{luas}")
            print(f"Keliling segitiga sama kaki: {keliling}")
        elif user == 2:
            alas = int(input("Masukan alas segitiga siku-siku :"))
            tinggi = int(input("Masukan tinggi segitiga siku :"))
            sisiMiring = int(input("Masukan sisi Miring segitiga siku-siku :"))
            luas = 0.5 * tinggi
            keliling = tinggi + alas + sisiMiring
            print(f"Luas segitiga siku-siku :{luas}")
            print(f"Keliling segitiga siku-siku: {keliling}")  
        else:
            print("input yang anda masukan salah!")
    except ValueError:
        print("Masukan angka yang valid")

# Fungsi lingkaran dan bola
def lingkaran():
    try:
        r = int(input("Masukkan jari-jari lingkaran: "))
        pi = 22 / 7 if r % 7 == 0 else 3.14
        d = 2 * r
        luas = pi * (r ** 2)
        kel = 2 * pi * r
        print(f"Luas lingkaran adalah: {luas}")
        print(f"Keliling lingkaran adalah: {kel}\nDiameter: {d}")
    except ValueError:
        print("Masukan angka yang valid")


#fungsi bola
def bola():
    try:
        r = int(input("Masukkan jari-jari bola: "))
        pi = 22 / 7 if r % 7 == 0 else 3.14
        volume = 4 / 3 * pi * (r ** 3)
        luas = 4 * pi * (r ** 2)
        print(f"Volume bola adalah: {volume}")
        print(f"Luas bola adalah: {luas}")
    except ValueError:
        print("Masukan angka yang valid")

        
#fungsi rumus balok       
def balok():
    try:
        panjang = int(input("Masukan panjang balok: "))
        lebar = int(input("Masukan lebar balok: "))
        tinggi = int(input("Masukan tinggi balok: "))
        luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
        volume = panjang * lebar * tinggi
        print(f"Luas balok adalah :{luas}")
        print(f"volume balok adalah :{volume}")
    except ValueError:
        print("Masukan angka yang valid")
        
 
#kencenderungan pusat data
def central_variance_position_data():
    try:
        print("Contoh: 10 20 30 10 .. .. ..")
        data = list(map(float, input("Masukan data anda: ").split()))
        N = len(data)
        mean = sum(data) / N
        print(f"Mean: {round(mean, 2)}")
        
        data.sort()  #mengurutkan data dari yang terkecil hingga terbesar(1, 2, 3, 4 .., ..)
        
        # Jika jumlah titik datanya genap, ambil rata-rata dari dua nilai tengahnya
        if N % 2 == 0:
            median = (data[N // 2 - 1] + data[N // 2]) / 2
            print(f"Median: {median}")
        else:
            # Jika jumlah titik datanya ganjil, ambil nilai tengahnya
            median = data[N // 2]
            print(f"Median: {median}")
        
        
        # Hitung kemunculan setiap nilai dalam kumpulan data
        count_dict = {}
        for value in data:
            if value in count_dict:
                count_dict[value] += 1
            else:
                count_dict[value] = 1
        
        # mencari modus
        modes = [key for key, value in count_dict.items() if value == max(count_dict.values())]
        
        if len(modes) == 1:
            print(f"Mode: {modes[0]}")
        else:
            print(f"Modes: {', '.join(map(str, modes))}")
                
        
        # Hitung variasi
        variance = sum((x - mean) ** 2 for x in data) / N
        print(f"Varian: {round(variance, 2)}")
        
        # Hitung deviasi standar (akar kuadrat dari varian)
        standard_deviation = variance ** 0.5
        print(f"Deviasi Standar: {round(standard_deviation, 2)}")
        
        #mencari range
        range = max(data) - min(data)
        print(f"range: {range}")
        
        # Hitung kuartil pertama, kedua, dan ketiga
        q1 = data[int(N * 0.25)]
        q2 = data[int(N * 0.5)]
        q3 = data[int(N * 0.75)]
        print(f"Kuartil 1: {q1}")
        print(f"Kuartil 2: {q2}")
        print(f"Kuartil 3: {q3}")
        
        # Hitung rentang interkuartil
        iqr = q3 - q1
        print(f"Rentang Interkuartil: {iqr}")
        print("---Make your own interpretation with your data---")
        
    except ValueError:
        print("Masukan angka yang valid")
   
#fungsi probabilitas
def probabilitas():
    try:
        user = int(input("1.Kombinasi\n2.Permutasi\nMasukan pilihan anda(Combination,Permutation): "))
        if user == 1:
            n = int(input("Masukan n: "))
            r = int(input("Masukan r: "))
            C = math.factorial(n) // (math.factorial(n-r) * math.factorial(r))
            print(f"{n} Combinasi {r} is: {C}")
        elif user == 2:
            n = int(input("Masukan n: "))
            r = int(input("Masukan r: "))
            P = math.factorial(n) // math.factorial(n-r)
            print(f"{n} Permutasi {r} is: {P}")
        else:
            print("Pilihan tidak valid. Silakan masukkan 1 atau 2.")
    except ValueError:
        print("Masukan input dengan benar")
    except KeyboardInterrupt:
        print("terimakasih program di hentikan")
        os.syetem("exit()")
        

while(True):
    try:
        pil = int(input("Masukan pilih menu anda: "))
        if pil == 1:
            persegi()
        elif pil == 2:
            persegiPanjang()
        elif pil == 3:
            jajarGenjang()
        elif pil == 4:
            segitiga()
        elif pil == 5:
            lingkaran()
        elif pil == 6:
            balok()
        elif pil == 7:
            bola()
        elif pil == 8:
            central_variance_position_data()
        elif pil == 9:
            probabilitas()
        else:
            print("Have a good day!")
            break
    except ValueError as e:
        print(f"Error: {e}. Mohon masukkan pilihan anda dengan benar.")
    except KeyboardInterrupt:
        print("Terima kasih. Program dihentikan.")
        break
        
if __name__ == '__main__':
    pass
