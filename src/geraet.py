class Geraet:
    anzahl_geraete = 0

    def __init__(self, name, stromverbrauch):
        self.name = name
        self.__status = False
        self._stromverbrauch = stromverbrauch

        Geraet.anzahl_geraete += 1

    def schalte_an(self):
        self.__status = True

    def schalte_aus(self):
        self.__status = False

    def get_status(self):
        return self.__status

    def __str__(self):
        status = "AN" if self.__status else "AUS"
        return (
            f"Gerät: {self.name} | "
            f"Status: {status} | "
            f"Verbrauch: {self._stromverbrauch}W"
        )