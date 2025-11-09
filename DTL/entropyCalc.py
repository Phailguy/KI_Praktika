import math
from collections import Counter


def berechne_entropie_daten(daten: str) -> float:
    """
    Berechnet die Shannon-Entropie einer Zeichenkette.

    Parameter:
        daten (str): Die Eingabezeichenkette.

    Rückgabewert:
        float: Entropie in Bit.
    """
    if not daten:
        return 0.0

    # Zähle Häufigkeiten der Symbole
    haeufigkeiten = Counter(daten)
    gesamt = len(daten)

    # Berechne Entropie
    entropie = 0.0
    for count in haeufigkeiten.values():
        p = count / gesamt
        entropie -= p * math.log2(p)

    return entropie



text = "O"
print(f"Entropie der Zeichenkette '{text}': {berechne_entropie_daten(text):.4f} Bit")


