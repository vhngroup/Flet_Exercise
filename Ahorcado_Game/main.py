import flet as ft

PALABRA_OBJETIVO = str("Desmayado").upper() # palabra objetivo "DESMAYADO"
palabra_oculta = ["_"]*len(PALABRA_OBJETIVO) # lista de _ de la misma longitud que la palabra objetivo
intentos_maximos = 8
intentos_restantes = intentos_maximos
ahorcado_images = [
    "./images/0.png",
    "./images/1.png",
    "./images/2.png",
    "./images/3.png",
    "./images/4.png",
    "./images/5.png",
    "./images/6.png",
    "./images/7.png",
    "./images/8.png",
]

def palabra_boton(letra, page, palabra_oculta_texto, ahorcado_images_visibles, mensaje_a_mostrar):
    letra = letra.upper()
    def on_click(e):
        global intentos_restantes
        e.control.disabled = True
        e.control.update()
        if letra in PALABRA_OBJETIVO:
            for idx, caracter in enumerate(PALABRA_OBJETIVO):
                if caracter == letra:
                    palabra_oculta[idx] = letra
            palabra_oculta_texto.value = " ".join(palabra_oculta)
            palabra_oculta_texto.update()

            if "_" not in palabra_oculta:
                mensaje_a_mostrar.color = "green"
                mensaje_a_mostrar.value = "--------- ¡Has ganado! ----------"
                mensaje_a_mostrar.update()
                deshabilitar_botones(page)
        else:
            intentos_restantes -= 1
            ahorcado_images_visibles.src = ahorcado_images[intentos_maximos - intentos_restantes]
            ahorcado_images_visibles.update()
            if intentos_restantes == 0:
                mensaje_a_mostrar.value = f"---- Haz Perdido, la palabra era {PALABRA_OBJETIVO} -----"               
                mensaje_a_mostrar.update()
                deshabilitar_botones(page)

    return ft.ElevatedButton(letra.upper(), on_click=on_click)

def deshabilitar_botones(page):
    for control in page.controls[1].controls:
        control.disabled = True
    control.update()

def main(page: ft.Page):
    page.title = "Ahorcado"
    palabra_oculta_texto = ft.Text(" ".join(palabra_oculta), size=28)
    ahorcado_images_visibles = ft.Image(src=ahorcado_images[0], width=400, height=400)
    mensaje_a_mostrar = ft.Text("Este es el mensaje", size=20, color="red")
    #alfabeto= "abcdefghijklmnopqrstuvwxyz"
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letra_boton = [palabra_boton(letra, page, palabra_oculta_texto, ahorcado_images_visibles, 
                                 mensaje_a_mostrar) for letra in alfabeto]
    page.window.width = 700
    page.window.height = 700
    page.window.resizable = False

    page.add(
        palabra_oculta_texto,
        ft.Row(controls=letra_boton, wrap=True, spacing=5),
        ahorcado_images_visibles,
        mensaje_a_mostrar
        )
    
ft.app(target=main)