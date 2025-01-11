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


def habitants(paisos: Paisos, x: float) -> int:
    """Retorna la suma de tots els habitants d’aquelles 
    paisos en paisos que tinguin almenys 2 províncies amb producte interior brut 
    inferior o igual a x."""

    suma_total = 0

    for pais in paisos:
        c = 0
        suma = 0
        for provincia in pais.provincies:
            suma += provincia.habitants
            if provincia.pib <= x:
                c += 1
        if c < 2:
            suma = 0
        suma_total += suma

    return suma_total
