from PySimpleGUI import PySimpleGUI as sg


# Layout
sg.theme('Reddit')
layout =[
    [sg.Text('1ª Hash'), sg.Input(key='h1')],
    [sg.Text('2ª Hash'), sg.Input(key='h2')],
    [sg.Button('Comparar', size=(46,3))],
    [sg.Output(size=(50,3))]
]



# Window
window = sg.Window('Py Hash Checker', layout)



# Ler eventos
while True:
        eventos, valores = window.read()

        hah_h1 = hash(valores['h1'])

        hah_h2 = hash(valores['h2'])

        if eventos == sg.WINDOW_CLOSED:
            break
        elif eventos == 'Comparar':
            if valores['h1'] == valores['h2'] and hah_h1 == hah_h2:
                print("\nAs Hash's são Iguais.")
            else:
                print("\nATENÇÃO as Hash's SÃO DIFERENTES!!!")










