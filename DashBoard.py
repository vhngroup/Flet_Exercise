import flet as ft

def main(page: ft.Page):
    page.title = "Tablero de Notas Adhesivas"
    page.padding =50
    page.theme_mode = "ligth"
    page.bgcolor= ft.colors.BLUE_GREY_800

    def add_note(e):
        new_note=create_note("Nueva Nota")
        grid.controls.append(new_note)
        page.update()
        
    def delete_note(note):
        grid.controls.remove(note)
        page.update()
    
    def create_note(text):
        note_content = ft.TextField(value=text, multiline=True, bgcolor=ft.colors.BLUE_GREY_50,)

        #Creamos el contenedor de las notas y al hacer click en delete llamamos a Delete Note
        note = ft.Container(
            content=ft.Column([note_content, 
                              ft.IconButton(icon=ft.icons.DELETE, on_click=lambda _: delete_note(note))]),
        width=200, height=200, bgcolor=ft.colors.BLUE_GREY_100, border_radius=20, padding=10,
        )
        return note   

    grid = ft.GridView(
        expand=True,
        max_extent=220,
        child_aspect_ratio=1, #relación de aspecto 1 a 1 cuadrado
        spacing=20, #Espacio en el button "abajo" entre cajetines
        run_spacing=20, #Espaciado lateral derecho entre cajetines
    )

    notes = [
        "Comprar Leche",
        "Comprar Agua",
        "Comprar Limonada"
    ]
    
    for note in notes:
        grid.controls.append(create_note(note))

    page.add(ft.Row([
        ft.Text("Tablero de notas", size=24, weight="bold", color=ft.colors.WHITE24),
        ft.IconButton(icon=ft.icons.ADD, on_click=add_note, icon_color=ft.colors.BLUE)

    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), grid)

ft.app(target=main)
