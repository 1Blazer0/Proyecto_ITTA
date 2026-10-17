from Desarrollo import funciones
from Desarrollo import interfaz
funciones.cargar_tareas()
funciones.cargar_correo()
print("Bienvenido!")
interfaz.msj_bienvenida()
while True:
    try:
        eleccion = int(input("Que desea hacer?\n0. Colocar correo electronico\n1. Ver la lista de tareas\n2. Agregar una tarea\n3. Eliminar una tarea\n4. Guardar tareas\n5. Enviar correo\n6. Salir del programa\n"))
        if eleccion > 6 or eleccion < 0:
            print("Eso no es una opcion valida!")
            interfaz.alerta_fuera_rango()
        elif eleccion == 0:
            if funciones.destinatario:
                print(f"Su correo electronico actual es: {funciones.destinatario}")
            funciones.pedir_correo()
        elif eleccion == 1:
            if len(funciones.lista_tarea) == 0:
                print("No hay nada en la lista todavia!")
                interfaz.alerta_vacia()
            else:
                funciones.mostrar_lista(interfaz.mostrar_lista_interfaz)
        elif eleccion == 2:
            funciones.crear_tarea(interfaz.tarea_repetida)
        elif eleccion == 3:
            funciones.eliminar_tarea(interfaz.alerta_vacia2,interfaz.alerta_fuera_rango,interfaz.alerta_tipo_incorrecto,interfaz.eliminar_tarea)
        elif eleccion == 4:
            funciones.guardar_tareas(interfaz.msj_guardar)
        elif eleccion == 5:
            if funciones.destinatario:
                funciones.enviar_correo(funciones.destinatario, funciones.mensaje_correo())
            else:
                print("No ha registrado un correo electronico.")
        elif eleccion == 6:
            funciones.guardar_correo()
            if funciones.lista_diferente():
                interfaz.alerta_guardado()
                funciones.guardar_lista_diferente(interfaz.alerta_oportunidades,interfaz.msj_guardar)
            break
    except ValueError:
        print("No puedo traducir tu opcion :(\nCargando...")
        interfaz.alerta_tipo_incorrecto()
print("Hasta la proxima!")