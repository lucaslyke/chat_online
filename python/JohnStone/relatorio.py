from playwright.sync_api import sync_playwright #pip install playwringht
from time import sleep 

producao = '//*[@id="main"]/nav/ul/li[9]/a/span'
consulta = '//*[@id="main"]/nav/ul/li[9]/ul/li[4]/a'
status = '//*[@id="consulta-producao"]/div/div[2]/div[1]/div/div/button/div/div/div'
aguardo = '//*[@id="consulta-producao"]/div/div[2]/div[1]/div/div/div/div/ul/li[1]/a'
em_producao = '//*[@id="consulta-producao"]/div/div[2]/div[1]/div/div/div/div/ul/li[2]/a'
celulas_internas = '//*[@id="consulta-producao"]/div/div[3]/div[1]/div/div/button'
marcar = '//*[@id="consulta-producao"]/div/div[3]/div[1]/div/div/div/div[1]/div/button[1]'
seta = '//*[@id="consulta-producao"]/div/div[1]/div/button[2]'
agrupar = '//*[@id="consulta-producao"]/div/div[1]/div/ul/li[1]/a'

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://dapic.webpic.com.br/')
    page.fill('xpath=//*[@id="form-autenticacao"]/div[1]/input', 'Johnstone')
    sleep(0.5)
    page.fill('//*[@id="form-autenticacao"]/div[2]/input', 'LUCAS LIMA')
    sleep(0.5)
    page.fill('//*[@id="form-autenticacao"]/div[3]/input', 'Lucas2023*')
    sleep(1)
    page.locator('//*[@id="form-autenticacao"]/button').click()
    sleep(2)
    #SELECIONAR A OPÇÃO DE PRODUÇÃO
    page.locator(producao).click()
    sleep(1)
    #SELECIONAR O STATUS DA CONSULTA
    page.locator(consulta).click()
    sleep(1)
    #SELECIONAR OS STATUS DA CONSULTA
    page.locator(status).click()
    sleep(1)
    #SELECIONAR AS QUE ESTÃO EM PRODUÇÃO
    page.locator(em_producao).click()
    #SELECIONAR AS QUE ESTÃO AGUARDANDO PRODUÇÃO

    sleep(30)
