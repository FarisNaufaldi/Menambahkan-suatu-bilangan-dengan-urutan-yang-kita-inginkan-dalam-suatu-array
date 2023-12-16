def memasukkan_angka(arr,angka,posisi):
    if posisi > len(arr):
        arr.append(angka)
    else:
        arr.insert(posisi,angka)
a = int(input("Kalian ingin ada berapa bilangan dalam suatu baris = "))
b = []
f = []
for i in range(a):
    c = int(input("Masukkan bilangan yang ingin dimasukkan = "))
    b.append(c)
    print(b)
    f.append(i)
e = int(input("Masukkan bilangan yang ingin anda masukkan ke dalam suatu urutan di dalam baris = "))
d = int(input(f"Anda ingin memasukkan {e} dalam urutan keberapa ? ada {len(f)} urutan anda ingin memasukkan nya kemana =  "))
memasukkan_angka(b,e,d)
print(b)