# Latihan 

# Kalkulator sederhana 
print("Kalkulator Sederhana")
print(20 * "=" + "\n")

angka_1 = float(input("masukan angka 1 ="))
operator = input("operator +, -, X, /) :")
angka_2 = float(input("masukan angka 2 ="))

# percabangannya
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "x":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah {hasil}")
else:
    print("Masukan yang bener dong!. aku pusying")

print("Akhir dari Program, terima gajih")


