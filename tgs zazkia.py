# Input umur
umur = int(input("Masukkan umur anda: "))

# Percabangan
if umur < 0:
    print("anda belum lahir")
elif umur < 18:
    print("anda belum cukup umur")
elif umur >= 18:
    print("anda cukup umur")

# Tambahan kondisi
if umur > 60:
    print("banyakin ibadah, bentar lagi mati")

print("Program selesai")