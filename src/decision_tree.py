"""Módulo que implementa un árbol de decisión simple basado en un umbral."""

from typing import List


def clasificar_numero(numero: int, umbral: int = 50) -> str:
    """Clasifica un número como 'Alto' o 'Bajo' según el umbral.

    Args:
        numero: Número entero a clasificar.
        umbral: Valor límite. Si numero >= umbral → 'Alto';
                si numero < umbral → 'Bajo'.

    Returns:
        'Alto' o 'Bajo' dependiendo de la comparación.
    """
    return "Alto" if numero >= umbral else "Bajo"


def clasificar_lista(numeros: List[int], umbral: int = 50) -> List[str]:
    """Clasifica una lista completa de números.

    Args:
        numeros: Lista de enteros.
        umbral: Umbral utilizado en la decisión.

    Returns:
        Lista de etiquetas ('Alto' o 'Bajo') en el mismo orden.
    """
    return [clasificar_numero(n, umbral) for n in numeros]
