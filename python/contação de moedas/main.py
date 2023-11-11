import PySimpleGUI as sg

layout [
    [sg.Text("Pegar cotação da moeda")],
    [sg.Input(key="moeda_origem", size=(10, 1))],
    [sg.Button("Pegar cotação"), sg.Button("Cancelar")],
    [sg.Text()]
]