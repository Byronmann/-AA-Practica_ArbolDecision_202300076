"""Programa principal que ejecuta el flujo del árbol de decisión simple."""

import time
import argparse
from src.data_loader import asegurar_archivo_numeros, cargar_numeros
from src.decision_tree import clasificar_lista


def main():
    """Ejecuta el flujo completo: generación/lectura, clasificación y reporte."""

    # Argumentos opcionales para permitir cambiar el umbral
    parser = argparse.ArgumentParser(description="Árbol de decisión simple.")
    parser.add_argument("--umbral", type=int, default=50,
                        help="Valor del umbral para clasificar (por defecto 50).")
    args = parser.parse_args()
    umbral = args.umbral

    inicio = time.time()

    # 1. Verificar o generar el archivo
    creado, semilla = asegurar_archivo_numeros()

    if creado:
        print(f"[INFO] Archivo generado automáticamente con semilla: {semilla}")
    else:
        print("[INFO] Archivo existente detectado. No se generó uno nuevo.")

    # 2. Cargar números
    numeros = cargar_numeros()
    print(f"[INFO] Se cargaron {len(numeros)} números.")

    # 3. Clasificar todos los números
    clasificaciones = clasificar_lista(numeros, umbral=umbral)

    # 4. Imprimir primeros 10 resultados
    print("\n=== Ejemplos de clasificación (primeros 10) ===")
    for num, etiqueta in zip(numeros[:10], clasificaciones[:10]):
        print(f"{num} → {etiqueta}")

    # 5. Conteo de resultados
    total_altos = clasificaciones.count("Alto")
    total_bajos = clasificaciones.count("Bajo")

    print("\n=== Conteos ===")
    print(f"Alto: {total_altos}")
    print(f"Bajo: {total_bajos}")

    # 6. Tiempo total
    fin = time.time()
    tiempo_total = fin - inicio
    print(f"\nTiempo total de ejecución: {tiempo_total:.4f} segundos")


if __name__ == "__main__":
    main()
