from .vuelo_bfs import buscar_solucion_BFS
from django.shortcuts import render

def vuelos_view(request):
    conexiones = {
        'Jiloyork': {'Celaya', 'Querétaro'},
        'Sonora': {'Zacatecas', 'Sinaloa'},
        'Sinaloa': {'Celaya', 'Sonora', 'Jiloyork'},
        'Querétaro': {'Monterrey', 'Tamaulipas', 'Zacatecas', 'Sinaloa', 'Jiloyork', 'Oaxaca'},
        'Celaya': {'Jiloyork', 'Sinaloa'},
        'Zacatecas': {'Sonora', 'Monterrey', 'Querétaro'},
        'Monterrey': {'Zacatecas', 'Sinaloa'},
        'Tamaulipas': {'Querétaro'},
        'Oaxaca': {'Querétaro'}
    }

    ruta = None

    if request.method == "POST":
        origen = request.POST.get("origen")
        destino = request.POST.get("destino")

        nodo_solucion = buscar_solucion_BFS(conexiones, origen, destino)

        if nodo_solucion:
            resultado = []
            nodo = nodo_solucion

            while nodo.get_padre() is not None:
                resultado.append(nodo.get_datos())
                nodo = nodo.get_padre()

            resultado.append(origen)
            resultado.reverse()

            ruta = resultado

    return render(request, "index.html", {"ruta": ruta})