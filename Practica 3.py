#MOISES RAMSES AGUILAR AYMA
#EJERCICIO1
import random

class Juego:
    def __init__(self, vidas):
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        print("Reiniciando partida...")
        pass

    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
            print(f"Nuevo récord: {self.record} vidas restantes")

    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            print(f"Te queda(n): {self.numeroDeVidas} vida(s)")
            return True
        else:
            print("No te quedan más vidas.")
            return False
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina el número secreto entre 0 y 10")

        while True:
            try:
                intento = int(input("Ingresa tu número: "))
            except ValueError:
                print("Entrada inválida. Debe ser un número.")
                continue
            if intento == self.numeroAAdivinar:
                print("Acertaste")
                self.actualizaRecord()
                break
            else:
                if not self.quitaVida():
                    print(f"😢 Has perdido. El número era: {self.numeroAAdivinar}")
                    break
                else:
                    if intento < self.numeroAAdivinar:
                        print("El número secreto es mayor")
                    else:
                        print("El número secreto es menor")
class Aplicacion:
    @staticmethod
    def main():
        print("Bienvenido al Juego Adivina Número")
        vidas = int(input("🔢 Ingresa el número de vidas: "))
        juego = JuegoAdivinaNumero(vidas)
        juego.juega()
if __name__ == "__main__":
    Aplicacion.main()
#MOISES RAMSES AGUILAR AYMA
#EJERCICIO2
import random

class Juego:
    def __init__(self, vidas):
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        pass

    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
            print(f"Nuevo récord: {self.record} vidas restantes")

    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            print(f"Te queda(n): {self.numeroDeVidas} vida(s)")
            return True
        else:
            print("No te quedan más vidas.")
            return False

class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0
    def validaNumero(self, numero):
        return 0 <= numero <= 10
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("\n Adivina el número secreto entre 0 y 10")

        while True:
            try:
                intento = int(input("Ingresa tu número: "))
            except ValueError:
                print("Entrada inválida. Debe ser un número")
                continue

            # Validación usando validaNumero
            if not self.validaNumero(intento):
                print("El número debe estar entre 0 y 10")
                continue
            if intento == self.numeroAAdivinar:
                print("Acertaste")
                self.actualizaRecord()
                break
            else:
                if not self.quitaVida():
                    print(f"Has perdido. El número era: {self.numeroAAdivinar}")
                    break
                else:
                    if intento < self.numeroAAdivinar:
                        print("El número secreto es mayor")
                    else:
                        print("El número secreto es menor")
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if not (0 <= numero <= 10):
            print("El número debe estar entre 0 y 10")
            return False
        if numero % 2 != 0:
            print("El número debe ser PAR")
            return False
        return True
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        """Valida que el número esté entre 0 y 10 y sea IMPAR"""
        if not (0 <= numero <= 10):
            print("El número debe estar entre 0 y 10")
            return False
        if numero % 2 == 0:
            print("El número debe ser IMPAR")
            return False
        return True
class Aplicacion:
    @staticmethod
    def main():
        print("Bienvenido a los 3 juegos de adivinación")
        
        juego_normal = JuegoAdivinaNumero(3)
        juego_par = JuegoAdivinaPar(3)
        juego_impar = JuegoAdivinaImpar(3)

        print("\n=== Juego 1: Adivina cualquier número ===")
        juego_normal.juega()

        print("\n=== Juego 2: Adivina un número PAR ===")
        juego_par.juega()

        print("\n=== Juego 3: Adivina un número IMPAR ===")
        juego_impar.juega()
if __name__ == "__main__":
    Aplicacion.main()