from geometri.Isi_Balok import VolumePersegiPanjang
from geometri.bujursangkar import BujurSangkar
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga
from geometri.volume_kerucut import VolumeKerucut

print('Menggunakan OOP!')

print('\nMenghitung Luas Persegi Panjang')
p1 = PersegiPanjang(10,3)
print(p1.info())
print(p1.hitung_luas())

print('\nMenghitung Luas Segitiga')
p2 = Segitiga(10,3)
print(p2.info())
print(p2.hitung_luas())

print('\nMenghitung Luas Bujursangkar')
p3 = BujurSangkar(10)
print(p3.info())
print(p3.hitung_luas())

print('\nMenghitung Volume Balok')
p4 = VolumePersegiPanjang(10,4,3)
print(p4.info())
print(p4.hitung_volume())

print('\nMenghitung Volume Kerucut')
p5 = VolumeKerucut(4,6)
print(p5.info())
print(p5.hitung_volume())