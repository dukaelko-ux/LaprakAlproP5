celcius_to_fahrenheit = lambda C: (9/5) * C + 32
celcius_to_reamur = lambda C: 0.8 * C

print("Pilih jenis konversi suhu:")
print("1. Celcius ke Fahrenheit")
print("2. Celcius ke Reamur")

try:
    pilihan = int(input("Masukkan pilihan (1 atau 2): "))

    if pilihan == 1:
        C = float(input("Masukkan suhu dalam Celcius: "))
        F = celcius_to_fahrenheit(C)
        print(f"Hasil konversi: {C}°C = {F}°F")
        
    elif pilihan == 2:
        C = float(input("Masukkan suhu dalam Celcius: "))
        R = celcius_to_reamur(C)
        print(f"Hasil konversi: {C}°C = {R}°R")
        
    else:
        print("Pilihan tidak valid. Harap masukkan angka 1 atau 2.")

except ValueError:
    print("Input harus berupa angka. Silakan coba lagi.")
