class VolumePersegiPanjang():
    def __init__(self, p, l, t):
    #fungsi yang dipanggil pertama kali
        self.p = p
        self.l = l
        self.t = t

    def info(self):
        return f'Komponen Volume persegi panjang dengan panjang = {self.p} lebar = {self.l} dan tinggi = {self.t}'

    def hitung_volume(self):
        return self.p * self.l * self.t