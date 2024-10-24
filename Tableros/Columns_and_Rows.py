import flet as ft

def main(page: ft.page):
    page.bgcolor = ft.colors.BLUE_GREY_600
    page.title = "Ejercicio de filas y Columnas"
    texto1 = ft.Text("texto 1", size=24, color=ft.colors.WHITE)
    texto2 = ft.Text("texto 2", size=24, color=ft.colors.WHITE)
    texto3 = ft.Text("texto 3", size=24, color=ft.colors.WHITE)

    fila_textos = ft.Row(
        controls=[texto1, texto2, texto3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50

    )
    
    boton1 = ft.FilledButton(text="Boton 1")
    boton2 = ft.FilledButton(text="Boton 2")
    boton3 = ft.FilledButton(text="Boton 3")

    fila_botones = ft.Row(
        controls=[boton1, boton2, boton3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50,
    )

    textos_columnas_1=[
        ft.Text("Columna 1 - Fila 1 ", size=18, color=ft.colors.WHITE),
        ft.Text("Columna 1 - Fila 2 ", size=18, color=ft.colors.WHITE),
        ft.Text("Columna 1 - Fila 3 ", size=18, color=ft.colors.WHITE),
    ]

    textos_columnas_2=[
    ft.Text("Columna 2 - Fila 1 ", size=18, color=ft.colors.WHITE),
    ft.Text("Columna 2 - Fila 2 ", size=18, color=ft.colors.WHITE),
    ft.Text("Columna 2 - Fila 3 ", size=18, color=ft.colors.WHITE),
    ]

    columna_texto1 = ft.Column(
    controls=textos_columnas_1
    )

    columna_texto2 = ft.Column(
    controls=textos_columnas_2
    )

    fila_columnas = ft.Row(
        controls=[columna_texto1, columna_texto2],
        alignment=ft.MainAxisAlignment.CENTER.CENTER,
        spacing=50,
    )

    page.add(fila_textos, fila_botones, fila_columnas)

ft.app(target=main)