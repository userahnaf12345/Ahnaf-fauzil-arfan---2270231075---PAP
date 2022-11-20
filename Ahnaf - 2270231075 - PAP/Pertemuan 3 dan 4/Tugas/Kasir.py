x = "=============== Terimakasih Guys ==============="

y = input("Are you want to input (yes/no) :")
print("")

if y == "yes":
    jalan = True
elif y == "no":
     jalan = False
     print(x)
elif y == "y":
     jalan = True
elif y == "n":
     jalan = False
     print(x)
else:
    print("!!!!!!!!!!!! INVALID INPUT Guys !!!!!!!!!!!!")
    print("!!!!!!!!!!!! INVALID INPUT Guys !!!!!!!!!!!!")
    print("!!!!!!!!!!!! INVALID INPUT Guys !!!!!!!!!!!!")
    print("!!!!!!!!!!!! INVALID INPUT Guys !!!!!!!!!!!!")

while(jalan == True):

    # Input Data Pembeli 
    print("============== Toko Ps yang ada Badaknya ==============")
    nama = input("Masukkan nama : ")
    alamat = input("Masukan alamat : ")
    no_telp = int(input("Masukan No.Telp : "))
    tanggal = input("Masukan tanggal : ")
    print("=======================================================")
    
    print("")    

    # Penampilan Daftar dan Harga Barang
    print("==================== Daftar Barang ====================")
    print("1. Ps5 Disc            Rp.9000000")
    print("2. Ps5 Digital         Rp.8000000")
    print("3. Ps4 Pro             Rp.5000000")
    print("4. Ps4                 Rp.4000000")
    print("=======================================================")
    
    # Input Nama Barang dan pemberian Harga Barang
    barang = str(input("Masukan Barang Pesanan : "))
    if barang == "Ps5 Disc":
        harga = 9000000
    elif barang == "Ps5 Digital":
        harga = 8000000
    elif barang == "Ps4 Pro":
        harga = 5000000
    elif barang == "Ps4":
        harga = 4000000 
    else:
        print("!!!!!!!!!!!! INVALID INPUT Guys !!!!!!!!!!!!")
        print("!!!!!!!!!!!! INVALID INPUT Guys !!!!!!!!!!!!")
        print("!!!!!!!!!!!! INVALID INPUT Guys !!!!!!!!!!!!")
        print("!!!!!!!!!!!! INVALID INPUT Guys !!!!!!!!!!!!")
           
    harga = harga

    # Input Jumlah Barang dan Total Harga Barang
    jumlah_pembelian = int(input("Masukan Jumlah Pembelian : "))
    total = int(jumlah_pembelian) * int(harga)
    print("=======================================================")

    print("")

    # Penampilan Struc pembelian 
    print("=================== Struc Pembelian ===================")
    print("Nama Pembeli       : ", nama) 
    print("Alamat Pembeli     : ", alamat)
    print("No.Telp Pembeli    : ", no_telp)
    print("Tangggal Pembelian : ", tanggal)
    print("Nama Barang        : ", barang)
    print("Jumlah Barang      : ", jumlah_pembelian,"Unit")
    print("Total Harga        :  " f"Rp.{total}")
    print("=======================================================")

    print("")

    y = input("Are you want to input again (yes/no) :")
    if y == "yes":
        jalan = True
    elif y == "y":
        jalan = True
    elif y == "n":
        jalan = False
        print(x)
    elif y == "no":
        jalan = False
        print(x)
    else:
        print("!!!!!!!!!!!! INVALID INPUT Guys !!!!!!!!!!!!")
        print("!!!!!!!!!!!! INVALID INPUT Guys !!!!!!!!!!!!")
        print("!!!!!!!!!!!! INVALID INPUT Guys !!!!!!!!!!!!")
        print("!!!!!!!!!!!! INVALID INPUT Guys !!!!!!!!!!!!")
        
    print("")
    



