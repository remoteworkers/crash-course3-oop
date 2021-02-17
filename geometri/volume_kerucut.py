from geometri.bangunruang import BangunRuang


class VolumeKerucut(BangunRuang):
    def __init__(self, r, t):
    #fungsi yang dipanggil pertama kali
        self.r = r
        self.t = t

    def info(self):
        return f'Komponen Volume Kerucut radius = {self.r} dan tinggi = {self.t}'

    def hitung_volume(self):
        return self.r**2 * self.t * 22/7 / 3