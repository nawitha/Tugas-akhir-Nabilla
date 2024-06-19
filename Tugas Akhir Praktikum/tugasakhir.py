from abc import ABC, abstractmethod

class AnggotaKpop(ABC):
    def __init__(self, nama, umur, posisi):
        self.nama = nama
        self.umur = umur
        self.posisi = posisi

    @abstractmethod
    def tampil(self):
        pass

class AksiKpop(ABC):
    @abstractmethod
    def menari(self):
        pass

    @abstractmethod
    def bernyanyi(self):
        pass

class Penari(AnggotaKpop, AksiKpop):
    def __init__(self, nama, umur, posisi, gaya_tari):
        super().__init__(nama, umur, posisi)
        self.gaya_tari = gaya_tari

    def tampil(self):
        print(f"{self.nama} sedang menari dengan gaya {self.gaya_tari}.")

    def menari(self):
        print(f"{self.nama} menari dengan enerjik dalam gaya {self.gaya_tari}.")

    def bernyanyi(self):
        print(f"{self.nama} bernyanyi sambil menari dengan gaya {self.gaya_tari}.")

class Vokalis(AnggotaKpop, AksiKpop):
    def __init__(self, nama, umur, posisi, rentang_vokal):
        super().__init__(nama, umur, posisi)
        self.rentang_vokal = rentang_vokal

    def tampil(self):
        print(f"{self.nama} sedang bernyanyi dengan rentang vokal {self.rentang_vokal}.")

    def menari(self):
        print(f"{self.nama} menari dengan halus mengikuti irama musik.")

    def bernyanyi(self):
        print(f"{self.nama} bernyanyi dengan indah dalam rentang vokal {self.rentang_vokal}.")

class Rapper(AnggotaKpop, AksiKpop):
    def __init__(self, nama, umur, posisi, gaya_rap):
        super().__init__(nama, umur, posisi)
        self.gaya_rap = gaya_rap

    def tampil(self):
        print(f"{self.nama} sedang nge-rap dengan gaya {self.gaya_rap}.")

    def menari(self):
        print(f"{self.nama} menari dengan keren dalam gaya {self.gaya_rap}.")

    def bernyanyi(self):
        print(f"{self.nama} bernyanyi sambil nge-rap dalam gaya {self.gaya_rap}.")

def tampilkan_penampilan(anggota: AnggotaKpop):
    anggota.tampil()
    anggota.menari()
    anggota.bernyanyi()

if __name__ == "__main__":
    penari = Penari("Hoshi", 28, "Main Dancer", "Hip Hop")
    vokalis = Vokalis("Dokyeom", 27, "Main Vocalist", "Tenor")
    rapper = Rapper("Mingyu", 27, "Main Rapper", "Trap")

    seventeen = [penari, vokalis, rapper]

    for anggota in seventeen:
        tampilkan_penampilan(anggota)
        print("-" * 57)
