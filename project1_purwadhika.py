# -*- coding: utf-8 -*-

"""
Capstone Project Modul 1 Purwadhika Data Science Machine Learning JCDSVL07
Yellow Pages Book Telephone Number PT Dawson
Yason Dawson Imawan
"""

#1. Tahun & Bulan Join
#2. Kode Cabang (Pusat 01 Daerah 02)
#3. Kode Jabatan (CEO 01, Co-CEO 02, VP 03, Manager/AsMen 04,Staf 05)
#4. Kode Divisi / Department (Keuangan 01, Operasional 02, Marketing 03
#                 , HR 04, IT 05)
#5. No Urut
#Contoh : [Tahun][Bulan][ Kode Cabang][Kode Jabatan] [No Urut]

daftar_kontak = {
    1: {
        'NIP': "201401010301001",
        'Nama': 'Tiara Malinka',
        'Departement': 'Finance and Accounting',
        'Jabatan': 'Vice President Finance and Accounting',
        'No_Telepon': 6281272251236
        },
    2: {
        'NIP': "201804020403011",
        'Nama': 'Jack Sherin',
        'Departement': 'Marketing',
        'Jabatan': 'Asisten Manager Pemasaran',
        'No_Telepon': 6289726372612     
        },
    3: {
        'NIP': "202101010505021",
        'Nama': 'Ruth Shinta',
        'Departement': 'IT',
        'Jabatan': 'Staff Data Science',
        'No_Telepon': 6281272251236      
        },
    4: {
        'NIP': "202012020402023",
        'Nama': 'Dian Susilo',
        'Departement': 'Operasional',
        'Jabatan': 'Manager Operasional Produk A',
        'No_Telepon': 628527872116     
        }
}

def tampilkan_opsi():
    print("Selamat Datang dibuku telepon PT Dawson")
    print("1. Menampilkan Semua Daftar Telepon")
    print("2. Merubah Daftar Telepon")
    print("3. Menambah Daftar Telepon")
    print("4. Menghapus Daftar Telepon")
    print("5. Keluar")

    pilih_opsi()

def pilih_opsi():
    repeat = True
    while repeat == True:
        try:
            opsi = int(input("Pilih Menu[1-5]: "))
        except ValueError:
            print("Masukkan Opsi yang Sesuai")
            opsi = 0
        if opsi > 0 and opsi < 6: repeat = False
        if opsi == 1:
          tampilkan_kontak()
          tampilkan_opsi()
        elif opsi == 2:
          print("\n==============")
          print("Masukkan Data yang akan Diperbaharui")
          print("==============")
          update_kontak()
          tampilkan_opsi()
        elif opsi == 3:
          print("\n===========")
          print("Masukkan Data yang akan Ditambahkan")
          print("===========")
          tambah_kontak()
          tampilkan_opsi()
        elif opsi == 4:
          hapus_kontak()
          tampilkan_opsi()
        elif opsi == 5:
          print("Terima Kasih dan Sampai Berjumpa Kembali")
          break
        else: 
          print("Pilihan Menu Tidak Tersedia")
          tampilkan_opsi()
          
         
def tampilkan_kontak():    
    print("==========================================================================================================================================================")
    print("|NIP                       | Nama                 | Departement                          | Jabatan                                       |No_Telepon      ")
    print("==========================================================================================================================================================")
    for kontak in daftar_kontak.values():
        print("|{NIP:<25} | {Nama:<20} | {Departement:<35}  | {Jabatan:<45} | {No_Telepon:<14}|"
              .format(NIP = kontak["NIP"], Nama =kontak["Nama"],
                      Departement=kontak['Departement'],
                      Jabatan=kontak["Jabatan"], 
                      No_Telepon=kontak["No_Telepon"]))      
    print("===========================================================================================================================================================")

def hapus_kontak():
  tampilkan_kontak()
  while True:
    Nama = str(input('Masukkan Nama yang akan Dihapus: '))
    check = str(input('Apakah Anda yakin Menghapus Data Tersebut? (Yes/No)')).capitalize()
    for nama_kontak, info_kontak in list (daftar_kontak.items()):
      if info_kontak['Nama']== Nama:
        del daftar_kontak[nama_kontak]
        tampilkan_kontak()
        print("Data '{}' Berhasil Dihapus!\n".format(Nama))
        break
    else:
      tampilkan_kontak()
      print('Data Tersebut Tidak Ditemukan!\n')
      break 

def update_kontak():
    update = False
    tampilkan_kontak()
    kontak_lama=str(input('Masukkan Nama yang Akan Diperbaharui: '))
    for kontak in daftar_kontak.values():
      if kontak_lama in kontak.values():
        print ("Data Tersebut {} Ditemukan!.\n".format(kontak_lama))
        try:
          NIP_baru = int(input('Masukkan NIP: '))
          nama_baru = str(input('Masukkan Nama: '))
          departement_baru = str(input('Masukkan Departement: '))
          jabatan_baru = str(input('Masukkan Jabatan: '))
          telepon_baru = int(input('Masukkan Telepon: '))
          #memperbaharui data
          kontak.update({"NIP": "{}".format(NIP_baru)})
          kontak.update({"Nama": "{}".format(nama_baru)})
          kontak.update({"Departement": "{}".format(departement_baru)})
          kontak.update({"Jabatan": "{}".format(jabatan_baru)})
          kontak.update({"telepon": telepon_baru})
          update=True
          print("Data '{}' Berhasil Diperbaharui ke '{}'.\n".format(kontak_lama, nama_baru))
        except ValueError:
          print("Masukkan Format yang Sesuai")
          break
    if update == False:
      print("Data Tidak Dapat Diproses. Masukkan Format yang Sesuai")
      tampilkan_opsi()



def tambah_kontak():
    kontak_baru = list(daftar_kontak.keys())[-1] + 1
    while True:
        try:
          NIP_baru = int(input('Masukkan NIP: '))
          nama_baru = str(input('Masukkan Nama: '))
          departement_baru = str(input('Masukkan Departement: '))
          jabatan_baru = str(input('Masukkan Jabatan: '))
          telepon_baru = int(input('Masukkan Telepon: '))
          daftar_kontak[kontak_baru] = {
                "NIP" : NIP_baru,
                "Nama": "{}" .format(nama_baru),
                "Departement": "{}" .format(departement_baru),
                "Jabatan": "{}" .format(jabatan_baru),
                "No_Telepon": telepon_baru
            }
          print("Data Tersebut {} Berhasil Dimasukkan!\n".format(nama_baru))
          break
        except ValueError:
            print("Data yang Dimasukkan Tidak Sesuai. Mohon Masukkan Sesuai dengan Format.\n")
            break


tampilkan_opsi()
