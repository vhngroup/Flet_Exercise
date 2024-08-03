import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_600
    page.title = "Mi Lista de Mercado"
    page.theme_mode = "ligth"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text("Mi Lista de Mercado con Flet", size=30, weight=ft.FontWeight.BOLD)
    def agregar_tarea(e):
        if campo_tarea.value:
            tarea = ft.ListTile(title = ft.Text(campo_tarea.value),  #Elementos de una lista
                                #Confirmamos si el checkbox esta seleccionado
                                leading=ft.Checkbox(on_change=seleccionar_tarea), bgcolor=ft.colors.WHITE,)
            tareas.append(tarea) 
            campo_tarea.value=""
            actualizar_lista()

    def seleccionar_tarea(e):
        #Iteramos cada una de las tareas, en lista de tareas
        seleccionadas= [t.title.value for t in tareas if t.leading.value]
        tareas_seleccionadas.value = "Tareas Seleccinadas: " +" ,".join(seleccionadas)
        page.update()

    def actualizar_lista():
        lista_tareas.controls.clear()
        lista_tareas.controls.extend(tareas)
        page.update()

    campo_tarea = ft.TextField(hint_text="Escribe una nueva tarea") #Entrada de texto
    boton_agregar = ft.FilledButton(text="Agregar una nueva nota", on_click=agregar_tarea)
    lista_tareas = ft.ListView(expand=1, spacing=4)# Ocupa todo el espacio dibujado
    tareas=[]
    tareas_seleccionadas = ft.Text("", size=20, weight=ft.FontWeight.BOLD)

    page.add(titulo, campo_tarea, boton_agregar, lista_tareas, tareas_seleccionadas)

ft.app(target=main)