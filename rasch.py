from math import sqrt


class Reshenie:
    def __init__(self, data):
        self.o = data[0]
        self.data = data[1:len(data)]
        self.data.sort()
        self.tpn = [12.7, 4.3, 3.2, 2.8, 2.6, 2.5, 2.4, 2.3, 2.3]
        self.vpn = [1.15, 1.46, 1.67, 1.82, 1.94, 2.03, 2.11, 2.18]
        self.n = len(self.data)
        self.data_p = ['' for i in range(self.n)]
        self.vilit = 0

        self.vilit_z = []
        self.vilit_sr = []
        self.vilit_sko = []

    def _srednee(self):
        sm = 0
        for i in range(len(self.data)):
            if self.data_p[i] != '-':
                sm += self.data[i]
        return sm/self.n

    def _SKO(self, sr):
        sm = 0
        for i in range(len(self.data)):
            if self.data_p[i] != '-':
                sm += (self.data[i] - sr)**2
        return sqrt(sm/self.n)

    def _promahi(self, sko, sr):
        for i in range(len(self.data)):
            if self.data_p[i] != '-':
                if abs(self.data[i] - sr)/sko <= self.vpn[self.n-3-self.vilit]:
                    self.data_p[i] = '+'
                else:
                    self.data_p[i] = '-'
                    check = False
                    self.vilit += 1
                    self.vilit_z.append(self.data[i])
                    self.vilit_sko.append(sko)
                    self.vilit_sr.append(sr)
                    self.n -= 1
                    return check
        return True

    def _sr_SKO(self, sko):
        return sko/sqrt(self.n)

    def _ochen_pogr(self, sr_sko):
        return self.tpn[self.n-2-self.vilit] * sr_sko

    def _pribor_pogr(self):
        return self.o/2

    def _poln_pogr(self, ochen_pogr, pribor):
        return sqrt(ochen_pogr**2 + pribor**2)

    def get_pogr(self):
        check = False
        sr, sko, sr_sko, ochen_pogr, pribor, poln = 0, 0, 0, 0, 0, 0

        while not check:
            sr = self._srednee()
            sko = self._SKO(sr)
            check = self._promahi(sko, sr)
            sr_sko = self._sr_SKO(sko)
            ochen_pogr = self._ochen_pogr(sr_sko)
            pribor = self._pribor_pogr()
            poln = self._poln_pogr(ochen_pogr, pribor)
            sr = self._srednee()

        return poln, self.data, self.data_p, self.vilit, self.vilit_z, self.vilit_sr, self.vilit_sko, sr, sko, sr_sko, ochen_pogr, pribor


