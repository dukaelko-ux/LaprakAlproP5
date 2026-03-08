def cek_angka(a, b, c):
    if a != b and b != c and a != c:
        if (a + b == c) or (a + c == b) or (b + c == a):
            return True
        else:
            return False
    else:
        return False

print(cek_angka(2, 3, 5))
print(cek_angka(4, 4, 8))
print(cek_angka(1, 2, 10)) 
