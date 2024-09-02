import flet as ft

def main(page: ft.Page):
    page.title= "Prospección de perfil de Usuario"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    titulo = ft.Text("Perfil de Usuario", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.PINK_ACCENT_400)
    
    preview = ft.Text("Completa el formulario para previzualizar", size=14)
    def update_preview(e):
        preview.value = f"""
Nombre: {name_input.value}
Edad: {age_DropDown.value}
Género: {gender_radio.value}
Intereses: {', '.join([c.label for c in interest_checkbox.controls if c.value])}
Modo Oscuro: {"Activado" if theme_switch.value else "Desactivado"}
        """
        page.update()

    name_input = ft.TextField(label="Nombre", border_radius=8, on_change=update_preview)
    age_DropDown = ft.Dropdown(
        label="Edad",
        options=[ft.dropdown.Option(str(age)) for age in range(18, 101)],
        border_radius=8, on_change=update_preview
    )

    gender_radio = ft.RadioGroup(
        content=ft.Row([
        ft.Radio(value="Masculino", label="Masculino"),
        ft.Radio(value="Femenino", label="Femenino"),
        ft.Radio(value="Otro", label="Otro")]),
        on_change=update_preview
    )

    interests=["Arte","Tecnologia","Musica","Comida","Cine","Viajes"]

    interest_checkbox = ft.Column([
        ft.Checkbox(label=interest, on_change=update_preview) for interest in interests
    ])

    def toggle_theme(e):
        if theme_switch.value:
            page.theme_mode = ft.ThemeMode.DARK
            titulo.color = ft.colors.GREEN_400
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            titulo.color = ft.colors.PINK_ACCENT_400
        page.update()

    theme_switch = ft.Switch(label="Modo Oscuro", on_change=lambda e: [toggle_theme(e), update_preview(e)])

    gender_radio.on_change = update_preview

    page.add(titulo, 
             name_input, 
             age_DropDown, 
             ft.Text("Genero", size=16, weight=ft.FontWeight.BOLD),
             gender_radio, 
             ft.Text("Intereses", size=16, weight=ft.FontWeight.BOLD),
             interest_checkbox,
             theme_switch,
             ft.Text("Previsualizacion de perfil", size=16, weight=ft.FontWeight.BOLD),
             preview
             )

ft.app(target=main)