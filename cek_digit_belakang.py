def cek_digit_belakang(a, b, c):
    if (a % 10 == b % 10) or (a % 10 == c % 10) or (b % 10 == c % 10):
        return True
    else:
        return False

try:
    input_user = input("Masukkan tiga angka (pisahkan dengan spasi): ")
    a, b, c = map(int, input_user.split())

    hasil = cek_digit_belakang(a, b, c)
    print(hasil)

except ValueError:
    print("Mohon masukkan tiga angka yang valid.")
