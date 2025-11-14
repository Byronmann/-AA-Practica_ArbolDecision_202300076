"""Módulo para manejar la lectura y generación del archivo de números."""

from pathlib import Path
import random
import time
from typing import List, Tuple

# Ruta del archivo de datos
RUTA_ARCHIVO = Path("data") / "numeros_1000.txt"

# Parámetros de generación
CANTIDAD_NUMEROS = 1000
MIN_NUMERO = 1
MAX_NUMERO = 100


def asegurar_archivo_numeros(ruta: Path = RUTA_ARCHIVO) -> Tuple[bool, int | None]:
    """Verifica si existe el archivo de números y lo genera si no existe.

    Si el archivo ya existe, no lo modifica.

    Args:
        ruta: Ruta del archivo a verificar o generar.

    Returns:
        Una tupla (creado, semilla):
        - creado (bool): True si se generó el archivo, False si ya existía.
        - semilla (int | None): Semilla usada para generar los números
          o None si el archivo ya existía.
    """
    if ruta.exists():
        return False, None

    ruta.parent.mkdir(parents=True, exist_ok=True)

    # Usamos la hora actual como semilla para poder mostrarla
    semilla = int(time.time())
    random.seed(semilla)

    numeros = [
        random.randint(MIN_NUMERO, MAX_NUMERO)
        for _ in range(CANTIDAD_NUMEROS)
    ]

    with ruta.open("w", encoding="utf-8") as archivo:
        for numero in numeros:
            archivo.write(f"{numero}\n")

    return True, semilla


def cargar_numeros(ruta: Path = RUTA_ARCHIVO) -> List[int]:
    """Carga los números desde el archivo de texto.

    Args:
        ruta: Ruta del archivo a leer.

    Returns:
        Lista de enteros leídos del archivo.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si alguna línea no se puede convertir a entero.
    """
    numeros: List[int] = []

    with ruta.open("r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                numeros.append(int(linea))

    return numeros
