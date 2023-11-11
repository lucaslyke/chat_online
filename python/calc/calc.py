from PySimpleGUI import PySimpleGUI as sg

def porcentagem(float_value: float) -> float:
    return float_value * 1.045
#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Digite o valor do tecido: '), sg.Input(key='valor_tecido', size=(8, 0))],
    [sg.Text('Digite o rendimento por KG: '), sg.Input(key='rendimento', size=(8, 0))],
    [sg.Button('Total'), sg.Text('', size=(30, 1), key='result')]
    
]
#Janela
janela = sg.Window('Tela de calculo de rendimento por peça', layout)

#Definindo o Icon
janela.set_icon('logo.ico')


#Ler evento
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Total':
        try:
            valor_tecido = valores['valor_tecido']
            rendimento = valores['rendimento']
            valor_tecido = valor_tecido.replace(",", ".")
            rendimento = rendimento.replace(",", ".")
            valor_tecido = float(valor_tecido)
            rendimento = float(rendimento)
            total = porcentagem(valor_tecido) / rendimento
            janela['result'].update(f"Resultado: R$:{total:.2f} por peça")
            janela['valor_tecido'].update('')
            janela['rendimento'].update('')
        except ValueError:
            sg.popup_error("Por favor, insira valores float válidos.")










 