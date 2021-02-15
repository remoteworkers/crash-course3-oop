class BujurSangkar():
    def __init__(self, s):
        self.s = s

    def info(self):
        return f'Ini adalah object dari bujursangka dengan sisi = {self.s} '

    def hitung_luas(self):
        return self.s ** 2