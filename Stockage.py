class Stockage:

    def __init__(self, capaMax, capaDispo):
        self.__capaMax = capaMax
        self._capaDispo = capaDispo

    def obtenirCapaDispo(self):
        return self.capaDispo

    def stocker(self, qte):
        self.capaDispo -= qte

    def estVide(self):
        return self.capaDispo == self.__capaMax

    def estRemplie(self):
        return self.capaDispo == 0
