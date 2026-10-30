from src.smartlampe import SmartLampe
from src.klimaanlage import Klimaanlage
from src.geraet import Geraet

lampe = SmartLampe("Wohnzimmerlampe", 15, 80)
klima = Klimaanlage("Klimaanlage", 1200, 16)

lampe.schalte_an()
klima.schalte_an()

print(lampe)
print(klima)

lampe.schalte_aus()
print("\nNach dem Ausschalten:")
print(lampe)

print(f"\nAnzahl Geräte: {Geraet.anzahl_geraete}")