from src.geraet import Geraet


class Klimaanlage(Geraet):

    def __init__(self, name, stromverbrauch, ziel_temperatur):
        super().__init__(name, stromverbrauch)
        self._ziel_temperatur = 22
        self.ziel_temperatur = ziel_temperatur

    @property
    def ziel_temperatur(self):
        return self._ziel_temperatur

    @ziel_temperatur.setter
    def ziel_temperatur(self, wert):
        if wert < 18:
            print("Warnung: Temperatur unter 18°C!")
        self._ziel_temperatur = wert

    def __str__(self):
        return (
            f"{super().__str__()} | "
            f"Zieltemperatur: {self._ziel_temperatur}°C"
        )