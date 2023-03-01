from Navire import Navire
from Stockage import Stockage

class Port:
    def __init__(self, tabStock):
        self.__tabStock = tabStock

    def dechargement(self, Navire):
        qteFret = Navire.obtenirQteFret()
        zones = self.__tabStock.sort(reverse=True)
        for zones in self.__tabStock:
            if qteFret <= Stockage.obtenirCapaDispo():
                Stockage.stocker(qteFret)
                Navire.decharger(qteFret)
                qteFret = Navire.obtenirQteFret()
                break
            else:
                capaDispo = Stockage.obtenirCapaDispo()
                Stockage.stocker(capaDispo)
                Navire.decharger(capaDispo)
                qteFret = Navire.obtenirQteFret()
