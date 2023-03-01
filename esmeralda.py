from Navire import Navire
from Port import Port
from Stockage import Stockage


class Test:
    def __init__(self):
        # Création des objets Stockage
        silo1 = Stockage(100)
        silo2 = Stockage(200)
        silo3 = Stockage(300)
        hangar1 = Stockage(1000)
        hangar1.stocker(500)  # le premier hangar est rempli à moitié
        hangar2 = Stockage(1000)
        hangar2.stocker(250)  # le deuxième hangar est rempli au quart
        
        # Création de l'objet Port
        port = Port()
        port.ajouteStockage(silo1)
        port.ajouteStockage(silo2)
        port.ajouteStockage(silo3)
        port.ajouteStockage(hangar1)
        port.ajouteStockage(hangar2)
        
        # Création de l'objet Navire
        esmeralda = Navire('0092493603', 'ESMERALDA', 'sac de riz', 1200)
        
        # Déchargement du navire
        decharge = port.dechargement(esmeralda)
        if decharge:
            print('Le navire ESMERALDA a été entièrement déchargé.')
        else:
            print('Le navire ESMERALDA n\'a pas été entièrement déchargé.')

test = Test()
