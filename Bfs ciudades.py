"""
PARTE 5 - BFS en un grafo de ciudades españolas
Módulo 2 · Algoritmos Avanzados con IA
"""

from collections import deque


# Grafo de ciudades españolas conectadas por tren
grafo = {
    "Madrid":     ["Toledo", "Segovia", "Valladolid"],
    "Toledo":     ["Madrid", "Cuenca"],
    "Segovia":    ["Madrid", "Valladolid", "Salamanca"],
    "Valladolid": ["Madrid", "Segovia", "Salamanca", "Burgos"],
    "Cuenca":     ["Toledo", "Valencia"],
    "Salamanca":  ["Segovia", "Valladolid"],
    "Burgos":     ["Valladolid"],
    "Valencia":   ["Cuenca"],
}


def bfs_camino_mas_corto(grafo, origen, destino):
    """
    Encuentra el camino más corto (en número de paradas) entre
    dos ciudades usando BFS (Búsqueda en Anchura).

    Complejidad temporal: O(V + E)
      - V = número de ciudades (vértices)
      - E = número de conexiones (aristas)
      BFS visita cada nodo y arista como máximo una vez.

    Args:
        grafo  (dict): Grafo como lista de adyacencia.
        origen (str):  Ciudad de inicio.
        destino (str): Ciudad de destino.

    Returns:
        list | None: Lista de ciudades del camino más corto,
                     o None si no existe ruta.
    """

    # --- Casos límite añadidos manualmente ---
    # 1. Ciudad de origen no existe en el grafo
    if origen not in grafo:
        print(f"Error: '{origen}' no existe en el grafo.")
        return None

    # 2. Ciudad de destino no existe en el grafo
    if destino not in grafo:
        print(f"Error: '{destino}' no existe en el grafo.")
        return None

    # 3. Origen y destino son la misma ciudad
    if origen == destino:
        print(f"Origen y destino son la misma ciudad: '{origen}'.")
        return [origen]

    # Cola BFS: cada elemento es el camino recorrido hasta ese nodo
    cola = deque([[origen]])

    # Conjunto de ciudades ya visitadas (evita ciclos)
    visitados = set([origen])

    while cola:
        camino_actual = cola.popleft()          # Extraemos el primer camino
        ciudad_actual = camino_actual[-1]       # La ciudad donde estamos

        # Exploramos los vecinos de la ciudad actual
        for vecino in grafo[ciudad_actual]:

            if vecino in visitados:
                continue                        # Ya visitado, lo saltamos

            nuevo_camino = camino_actual + [vecino]

            if vecino == destino:               # ¡Encontrado!
                return nuevo_camino

            visitados.add(vecino)
            cola.append(nuevo_camino)

    # 4. Grafo desconectado: no existe ruta entre origen y destino
    print(f"No existe ruta entre '{origen}' y '{destino}'.")
    return None


def mostrar_resultado(origen, destino, camino):
    """Imprime el resultado de forma legible."""
    if camino:
        paradas = len(camino) - 1
        ruta = " → ".join(camino)
        print(f"\n  Ruta: {ruta}")
        print(f"  Paradas: {paradas}")
    else:
        print(f"\n  Sin ruta de '{origen}' a '{destino}'.")


# ──────────────────────────────────────────────
#  PRUEBAS
# ──────────────────────────────────────────────
if __name__ == "__main__":

    print("=" * 55)
    print("  BFS — Camino más corto entre ciudades españolas")
    print("=" * 55)

    # Caso principal del ejercicio
    print("\n[1] Madrid → Valencia")
    camino = bfs_camino_mas_corto(grafo, "Madrid", "Valencia")
    mostrar_resultado("Madrid", "Valencia", camino)

    # Caso: misma ciudad
    print("\n[2] Madrid → Madrid (misma ciudad)")
    camino = bfs_camino_mas_corto(grafo, "Madrid", "Madrid")
    mostrar_resultado("Madrid", "Madrid", camino)

    # Caso: ciudad no existente
    print("\n[3] Madrid → Sevilla (ciudad inexistente)")
    camino = bfs_camino_mas_corto(grafo, "Madrid", "Sevilla")
    mostrar_resultado("Madrid", "Sevilla", camino)

    # Caso: destino de un extremo del grafo
    print("\n[4] Valencia → Burgos")
    camino = bfs_camino_mas_corto(grafo, "Valencia", "Burgos")
    mostrar_resultado("Valencia", "Burgos", camino)

    # Caso: ruta corta directa
    print("\n[5] Segovia → Salamanca")
    camino = bfs_camino_mas_corto(grafo, "Segovia", "Salamanca")
    mostrar_resultado("Segovia", "Salamanca", camino)

    print("\n" + "=" * 55)
    print("  Todos los tests completados.")
    print("=" * 55)