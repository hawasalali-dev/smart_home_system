from src.geraet import Geraet


class SmartLampe(Geraet):

    def __init__(self, name, stromverbrauch, helligkeit=0):
        super().__init__(name, stromverbrauch)
        self.helligkeit = helligkeit

    def schalte_aus(self):
        super().schalte_aus()
        self.helligkeit = 0

    def __str__(self):
        return f"{super().__str__()} | Helligkeit: {self.helligkeit}%"