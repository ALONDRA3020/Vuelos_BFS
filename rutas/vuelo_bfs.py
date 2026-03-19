from .arbol import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []

    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)

    while (not solucionado) and len(nodos_frontera) != 0:

        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)

        # Si encontramos la solución
        if nodo.get_datos() == solucion:
            return nodo

        else:
            dato_nodo = nodo.get_datos()
            lista_hijos = []

            # Expandir nodos (conexiones de vuelos)
            if dato_nodo in conexiones:
                for un_hijo in conexiones[dato_nodo]:
                    hijo = Nodo(un_hijo)
                    lista_hijos.append(hijo)

                    if (not hijo.en_lista(nodos_visitados) and
                        not hijo.en_lista(nodos_frontera)):
                        nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

    return None