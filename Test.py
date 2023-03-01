from Navire import Navire
from Port import Port
from Stockage import Stockage

navire = Navire("0092493603", "ESMERALDA", "sac de riz", 1500)

silo1 = Stockage(100)
silo2 = Stockage(200)
silo3 = Stockage(300)

hangar1 = Stockage(1000)
hangar2 = Stockage(1000)

hangar1.stocker(500)
hangar2.stocker(750)

zonesDeStockage = [silo1, silo2, silo3, hangar1, hangar2]

port = Port(zonesDeStockage)

port.dechargement(navire)

print("La quantité Fret restant : ",navire.obtenirQteFret())


"""class Test:
  def __init__(self):
    navire = Navire("0092493603", "ESMERALDA", "sac de riz", 1200)

    silo1 = Stockage(100)
    silo2 = Stockage(200)
    silo3 = Stockage(300)

    hangar1 = Stockage(1000)
    hangar2 = Stockage(1000)

    hangar1.stocker(500)
    hangar2.stocker(250)

    zonesDeStockage = [silo1, silo2, silo3, hangar1, hangar2]

    port = Port(zonesDeStockage)

    port.dechargement(navire)

    print("La quantité Fret restant : ",navire.obtenirQteFret()) """
