#!/usr/bin/python

import random
import string
import sys
import os
import time

kata = list(string.ascii_lowercase)
angka = list(range(10))
a26 = list(range(26))

def spab(x):
 for i in range(x):
  print(" ")
 
#memasukkan input
print("tulis pesan yang ingin dienkripsi.(pesan dan password hrs sama panjang)")
pesan = input("")
print("masukkan password untuk kriptografi")
password = input("")



#membuat dicti kata ==> angka dan sebaliknya
pesan = list(pesan.lower())


mldi = 0
dicti = {}
dictii = {}

for lala in range(26):
 dicti[kata[mldi]] = mldi
 dictii[mldi] = [kata[mldi]]
 mldi += 1
spasi = " "
kata.append(spasi)
dicti[spasi] = 99
#print(dicti)
a = print(" ")
#print(dictii)
#time.sleep(1)

#membuat dictionary yang terenkripsi

#membuat pass dan pesan jadi list
pesann = list(pesan)
passwordd = list(password)
ang1 = len(pesann)
ang2 = len(passwordd)
if ang1 != ang2:
 print("digit pesan dan password harus sama(spasi termasuk digit)")
 print("contoh: ")
 print("pesan: program kevin keren (18 digit)")
 print("password: mantap jiwa banget (18 digit)")
 print("digitnya sama baru bisa")
 spab(5)
 exit()
nol = 0
noll = 0
trus = 1
pja = []
sja = []

#print(dictii)
#mencocokan list dan dictionary
print(dictii)
spab(10)
#untuk pesan
for vvv in range(ang1):
 if pesann[nol] in dicti:
  pja.append(dicti[pesann[nol]])
 if pesann[nol] in dictii:
  pja.append(dictii[pesann[nol]])
 nol += 1  
# if pja[nol] in dictii:
#  pja.append(dictii[pesann[nol]])
# else:
#  print('error')


#untuk password
for vvv in range(ang2):
 if passwordd[noll] in dicti:
  sja.append(dicti[passwordd[noll]])
 if passwordd[noll] in dictii:
  sja.append(dictii[passwordd[noll]])
 noll += 1

print("//////////")
print(dictii)
print("/////////")
spab(10)
print(pja)
spab(5)
print(sja)
print("=====")


#messege and password is match with dictionary! time to ecnrypt them(keren)
huff = 0
enkripsi = []
for nnn in range(ang1):
  enkripsi.append((pja[huff]) + (sja[huff]))
  huff += 1

print("pesan terenkripsi:")
print(enkripsi)
spab(10)











































"""
#pesan
convp = []
mls = 0
for sym in pesan:
 a = dicti[(pesan[mls])]
 convp.append(a)
 mls += 1
#password
convpp = []
mlss = 0
for symm in pesan:
 zz = dicti[(password[mlss])]
 convpp.append(zz)
 mlss += 1

print(convp)
print(" ")
print(convpp)
#pesan dan password sudah menjadi convp dan convpp.time to encrypt them!
#mengkalkulasi
mlbg = 0
for word in convp:
 convp[mlbg] += convpp[mlbg]
 mlbg += 1


print(convp)
#print(dicti)
print(" ")
print(dictii)

"""
