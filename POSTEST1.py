# Login Sederhana menggunakan Nama, NIM, Pin
nama = input("Masukan nama anda: ")

#Memasukan NIM dan wajib menggunakan angka
while True:
    try:
        nim = int(input("Masukan NIM anda: "))
        break  # Keluar dari loop jika NIM valid (berupa integer)
    except ValueError:
        print('=========== NIM harus berupa angka! Silahkan coba lagi ===========')

# Memasukan PIN dan wajib menggunakan angka, Jika memasukan type data selain integer maka akan diulang meminta int
while True:
    try:
        pin = input('Masukkan PIN (harus 6 angka): ')
        if len(pin) != 6 or not pin.isdigit(): #diperiksa apakah PIN yang user input memenuhi dua kondisi berikut
            raise ValueError
    except ValueError:
        print('=========== PIN harus terdiri dari 6 angka! Silahkan coba lagi ===========')
        continue
    print(f"Hola!, Selamat Datang {nama} dengan PIN {pin}")  # Cetak Sapaan
    break
print("\n")  # Menambahkan Space line baru


# Pemilihan Operasi
print("===========Kalkulator Segitiga Pythagoras===========")
print("[1]. Mencari sisi Alas")
print("[2]. Mencari sisi Tegak")
print("[3]. Mencari sisi Miring")

# apabila user input tidak sesuai, maka user akan diarahkan untuk menginput yang benar
while True:
    operasi = input("Silakan Pilih Operasi yang diinginkan : ")

    if operasi == "1":  # operasi sisi alas
        sisi_miring = float(input("Input Sisi Miring : "))
        sisi_tegak = float(input("Input Sisi Tegak : "))
        sisi_alas = (sisi_miring**2 - sisi_tegak**2)**0.5  # Kalkulator perhitungan/Rumus
        print(f"Panjang Sisi Alas adalah {sisi_alas}")
        print("-----------------Selesai-----------------")

    elif operasi == "2":  # operasi sisi tegak
        sisi_miring = float(input("Input Sisi Miring : "))
        sisi_alas = float(input("Input Sisi Alas : "))
        sisi_tegak = (sisi_miring**2 - sisi_alas**2)**0.5  # Kalkulator perhitungan/Rumus
        print(f"Panjang Sisi Tegak adalah {sisi_tegak}")
        print("-----------------Selesai-----------------")

    elif operasi == "3":  # operasi sisi miring
        sisi_alas = float(input("Input Sisi Alas : "))
        sisi_tegak = float(input("Input Sisi Tegak : "))
        sisi_miring = (sisi_alas**2 - sisi_tegak**2)**0.5  # Kalkulator perhitungan
        print(f"Panjang Sisi Tegak adalah {sisi_miring}")

    else:  # Jika user menginputkan pilihan operasi selain 1,2,3 maka akan diulang ke pemilihan operasi
        print("Pilihan tidak sesuai, Silakan coba lagi")