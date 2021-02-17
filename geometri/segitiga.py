#from geometri.bangunruang import BangunRuang
from geometri.bangunruang import BangunRuang


class Segitiga(BangunRuang):

    def __init__(self, alas, tinggi):
    #fungsi yang dipanggil pertama kali
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return f'Ini adalah object dari segitiga dengan alas = {self.alas} dan tinggi = {self.tinggi}'

    def hitung_luas(self):
        return self.alas * self.tinggi /2
