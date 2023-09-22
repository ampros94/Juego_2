avanzar = {
    "bienvenida": "Bienvenido al laberinto del minotauro, al entrar serás perseguido por él, recuerda que hay trampas. Si te alcanza el minotauro o activas una trampa, pierdes. Escribe 'entrar' para continuar... ",
    "zona1": "¿A donde iras primero? izq, der, cen... ",
    "zona2": "Te alejaste un poco de Minotauro. A donde irar ahora? izq, der... ",
    "zona3": "Te sigues alejado del Minorauro. cual sera tu proxima eleccion? der, izq... ",
    "zona4": "Vas muy bien, pero sigue detras de ti el minutaruro. que elegiras ahora? izq, cen... ",
    "zona5": "Muy bien, ahora te encontraste con un hueco en una pared. que elegiras ahora? izq(Hueco), der, cen... ",
    "zona6": "Estas muy cerca de salir. Que camino tomaras ahora? der, cen... ",
}

perder = {
    "bienvenida": "¡Cobarde, huyes antes de entrar!",
    "zona1": {
        "msg1": "Activaste una trampa. Has perdido...",
        "msg2": "Callejon sin salida. Has perdido...",
    },
    "zona2": "Activaste una trampa. Has perdido...",
    "zona3": "Caiste en una fosa. Has perdido...",
    "zona4": "Te tropiesas y te alcanza el minotauro. Has perdido...",
    "zona5": {
        "msg1": "En el hueco habia una serpiente y te a mordido. Has perdido...",
        "msg2": "Callejon sin salida y te alcanza el minotauro. Has perdido..."
    },
    "zona6": "Activaste una trampa. Has perdido..."
}


class Laberinto:
    def __init__(self):
        self.camino = ["entrar", "cen", "izq", "izq", "cen", "der", "cen"]


class Juego:
    def __init__(self, nuevoLaberinto):
        self.laberinto = nuevoLaberinto
        self.listaPasos = []
        self.textosPerder = []
        self.pasos()
        
    def iniciarJuego(self):
        for index in range(len(self.laberinto)):
            paso = input(avanzar[self.listaPasos[index]])
            if self.laberinto[index] != paso:
                if index in [1, 5, 3]:
                    print(self.textosPerder[index])
                    print(perder[self.textosPerder[index]]["msg1"] if self.laberinto[index] == "der" else perder[self.textosPerder[index]]["msg2"])
                else:
                    print(perder[self.textosPerder[index]])
                break
            elif len(self.laberinto) - 1 == index:
                print("¡Lograste salir del laberinto!")

    def pasos(self):
        listaPasosVictoria = list(avanzar.keys())
        listaTextosDerrota = list(perder.keys())
        self.listaPasos = listaPasosVictoria
        self.textosPerder = listaTextosDerrota


laberinto1 = Laberinto()
juego1 = Juego(laberinto1.camino)
juego1.iniciarJuego()