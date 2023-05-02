
import PySimpleGUI as sg

def ejecutar_inicio ():
	layout = [[sg.Button('Nuevo Perfil', key = '-NUEVO_PERFIL-')],
		  [sg.Button('Menu Principal', key = '-MENUPRINCIPAL-', button_color= 'red')],
		  [sg.Button('Editar Perfil',key = '-Configuracion-')]]
	window = sg.Window('UNLP Images',layout)
	while True:
	    event,value= window.read()
	    if event[0] == sg.WIN_CLOSED:
		break
	    elif event[0] == '-NUEVO_PERFIL-':
	    elif event[0] == '-MENUPRINCIPAL-':
	    elif event[0] == '-Configuracion-':
	
	window.close()
