import PySimpleGUI as sg

def ejecutar_menu_inicio():
    size_button = (25,3)
    layout = [[sg.Column(
                [
                [sg.Button("Etiquetar Imagen",key = "-ETIQUETAR_IMAGEN-", size= size_button)],
                [sg.Button("Generar Meme", key = "-GENERAR_MEME-",size = size_button)],
                [sg.Button("Generar Collage", key = "-GENERAR_MEME-",size = size_button)],
                [sg.Button("Salir", key = "-SALIR-",size = size_button)],
                ], element_justification = 'c', pad = ((50,50),(160,160))
                )
            ]]
    window = sg.Window("Menu Principal", layout,size=(800,600), element_justification='center')

    while True:
        event = window.read()
        if ((event[0] == sg.WIN_CLOSED) or ( event[0] == "-SALIR-")):
            break
        #elif event[0] == "":
        #elif event[0] == "":
        #elif event[0] == "":
    window.close()    

