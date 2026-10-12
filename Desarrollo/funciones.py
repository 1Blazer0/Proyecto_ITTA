import json
import datetime
lista_tarea = []
lista_guardada = []
def mostrar_lista(lista_interfaz=None):
    if lista_interfaz:
        lista_interfaz(lista_tarea)
    contador = 1
    for tarea in lista_tarea:
        print(f"{contador}. {tarea}")
        contador += 1
def agregar_tarea(tarea):
    lista_tarea.append(tarea)
    print(f"La tarea ({tarea}) ha sido agregada con exito!\nActualmente tienes {len(lista_tarea)} tareas pendientes.")
def crear_tarea(tarea_repetida=None):
    tarea = input("Que tarea desea agregar?\n")
    if tarea not in lista_tarea:
        agregar_tarea(tarea)
    else:
        print(f"La tarea ({tarea}) ya esta en la lista")
        if tarea_repetida:
            tarea_repetida(tarea)
def eliminar_tarea(alerta_vacia2=None,alerta_rango=None,alerta_tipo=None,eliminar_tarea=None):
    if len(lista_tarea) == 0:
        print("No hay ninguna tarea aun!")
        if alerta_vacia2:
            alerta_vacia2()
    else:
        mostrar_lista()
        error = 0
        while True:
            try:
                if error == 3:
                    mostrar_lista()
                    error = 0
                opcion = int(input("Que tarea desea eliminar?\nEscriba 0 para no eliminar ninguna: "))
                if opcion == 0:
                    print("Ninguna tarea ha sido eliminada")
                    break
                elif opcion < 1 or opcion > len(lista_tarea):
                    print("Esa opcion no es valida!")
                    if alerta_rango:
                        alerta_rango()
                    error += 1
                else:
                    tarea_eliminada = lista_tarea.pop(opcion-1)
                    print(f"La tarea ({tarea_eliminada}) ha sido eliminada con exito!")
                    if eliminar_tarea:
                        eliminar_tarea(tarea_eliminada)
                    break
            except ValueError:
                print("No puedo traducir tu opcion :(")
                if alerta_tipo:
                    alerta_tipo()
                error += 1
def cargar_tareas():
    global lista_tarea, lista_guardada
    try:
        with open("tareas.json", "r") as archivo:
                lista_tarea = json.load(archivo)
                lista_guardada = lista_tarea.copy()
        print("Tus tareas han sido cargadas exitosamente!")
    except FileNotFoundError:
            lista_tarea = []
            lista_guardada = []
def guardar_tareas(msj_guardar=None):
        global lista_guardada
        with open("tareas.json", "w") as archivo:
            json.dump(lista_tarea, archivo)
            lista_guardada = lista_tarea.copy()
            print("Tus tareas han sido guardadas con exito!")
            if msj_guardar:
                msj_guardar()
def lista_diferente():
    return lista_guardada != lista_tarea
def guardar_lista_diferente(alerta_oportunidades=None,msj_guardado=None):
    oportunidades = 5
    while True:
        guardar = input("Detectamos cambios no guardados. Desearia guardarlos?\n(Y/N): ").lower()
        if guardar == "y" or guardar == "ye" or guardar == "yes":
            guardar_tareas()
            if msj_guardado:
                msj_guardado()
            break
        elif guardar == "n" or guardar == "no":
            print("Cerrando sin guardar...")
            break
        elif oportunidades > 2:
            oportunidades -= 1
            print(f"Eso no es una opcion!\nTiene {oportunidades} oportunidades mas para guardar.")
            if alerta_oportunidades:
                alerta_oportunidades(oportunidades)
        elif oportunidades == 2:
            oportunidades -= 1
            print(f"Eso no es una opcion!\nEsta es su ultima oportunidad para guardar.")
            alerta_oportunidades(oportunidades)
        else:
            print("Cometio muchos errores!\nCerrando sin guardar...")
            break