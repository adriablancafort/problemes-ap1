from typing import TypeAlias
from dataclasses import dataclass

@dataclass
class Provincia:
    nom: str
    capital: str
    habitants: int
    area: int
    pib: float


@dataclass
class Pais:
    nom: str
    capital: str
    provincies: list[Provincia]


Paisos: TypeAlias = list[Pais]


def pib(paisos: Paisos, inicial: str, densitat: float) -> float:
    """Retorna la suma dels productes interiors bruts de totes les províncies amb 
    densitat estrictament superior a densitat de tots els paisos en paisos 
    que comencin per la lletra inicial."""

    pib_total = 0.0

    for pais in paisos:
        if pais.nom[0] == inicial:
            for provincia in pais.provincies:
                densitat_provincia = provincia.habitants / provincia.area
                if densitat_provincia > densitat:
                    pib_total += provincia.pib

    return pib_total

# Exemple
paisos_example = [
    Pais("Spain", "Madrid", [Provincia(
        "Barcelona", "Barcelona", 5000000, 1000, 2000000)]),
    Pais("France", "Paris", [
        Provincia(
        "Paris", "Paris", 6000000, 1200, 3200000),
        Provincia(
        "Touluse", "Touluse", 2000000, 800, 2000000)
        ]),
]

result = pib(paisos_example, "F", 300)
print(result)
