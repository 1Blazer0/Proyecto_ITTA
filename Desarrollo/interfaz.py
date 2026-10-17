import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
def obtener_fecha(cal, ventana):
    fecha = cal.get_date()
    print("Fecha seleccionada:", fecha)
    ventana.withdraw()
    messagebox.showinfo("Fecha", f"La fecha seleccionada fue: {fecha}")
    ventana.destroy()
    return fecha
def seleccionar_fecha():
    ventana = tk.Tk()
    ventana.title("Seleccionar fecha")
    cal = Calendar(ventana, selectmode="day", date_pattern="dd/mm/yyyy")
    cal.pack(pady=20)
    boton = tk.Button(ventana, text="Aceptar", command=lambda: obtener_fecha(cal, ventana))
    boton.pack(pady=10)
    ventana.mainloop()
def msj_guardar():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Guardar", f"¡Tus tareas han sido guardadas!")
    root.destroy()
def eliminar_tarea(tarea):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Eliminar", f"¡La tarea ({tarea}) ha sido eliminada!")
    root.destroy()
def tarea_repetida(tarea):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", f"¡La tarea ({tarea}) ya esta en la lista!")
    root.destroy()
def ventana(interfaz):
    interfaz.title("Gestor de tareas")
    interfaz.geometry("1080x1920")
def msj_bienvenida():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Bienvenido!", "¡Eliga la opcion que desee!")
    root.destroy()
def ayuda():
    root = tk.Tk()
    root.withdraw()
    respuesta = messagebox.askyesno("Guardar cambios", "¿Desea guardar los cambios realizados a la lista de tareas?")
    root.destroy()
    return respuesta
def alerta_guardado():
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning("Advertencia", "¡Detectamos cambios no guardados!")
    root.destroy()
def alerta_vacia2():
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", "¡No hay ninguna tarea aun!")
    root.destroy()
def alerta_vacia():
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", "¡No hay nada en la lista todavía!")
    root.destroy()
def alerta_tipo_incorrecto():
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", "No puedo traducir tu opcion :(")
    root.destroy()
def alerta_fuera_rango():
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", "¡Esa no es una opcion!")
    root.destroy()
def alerta_oportunidades(oportunidades):
    if oportunidades > 1:
        messagebox.showwarning("Advertencia", f"Le quedan {oportunidades} oportunidades para guardar.")
    else:
        messagebox.showwarning("Advertencia", "Esta es su ultima oportunidad para guardar.")
def opciones(interfaz):
    y=0
    textos_opciones = ["1. Ver la lista de tareas","2. Agregar una tarea","3. Eliminar una tarea","4. Guardar tareas","5. Salir del programa"]
    for texto in textos_opciones:
        opcion = tk.Label(interfaz, text=texto, font=("Arial", 30, "bold"))
        opcion.place(x=0,y=y)
        y +=50
def mostrar_lista_interfaz(lista_tareas):
    root = tk.Tk()
    root.title("Lista de tareas")
    root.geometry("600x600")
    contador = 1
    y=0
    if len(lista_tareas) > 15:
        for tarea in lista_tareas:
            tarea_label = tk.Label(root, text=f"{contador}. {tarea}", font=("Arial", 10))
            tarea_label.place(x=0,y=y)
            contador += 1
            y += 20
    for tarea in lista_tareas:
        tarea_label = tk.Label(root, text=f"{contador}. {tarea}", font=("Arial", 14))
        tarea_label.place(x=0,y=y)
        contador += 1
        y += 30
    root.destroy()