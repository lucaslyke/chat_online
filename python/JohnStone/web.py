"""
INSTALAR A BIBLIOTECA PLAYWRINGHT
RODAR O COMANDO "playwright install" no prompt
"""


from playwright.sync_api import sync_playwright #pip install playwringht
from time import sleep 
ref = '00084'
valor = '40'
atacado = '//*[@id="grid-tabela-preco"]/tbody/tr[1]/td[1]/button/i'
varejo = '//*[@id="grid-tabela-preco"]/tbody/tr[2]/td[1]/button'
#tamanhos
tam_P = '//*[@id="form-produto-tabela-preco"]/div[3]/table/tbody/tr[2]/td[2]/input'
tam_M = '//*[@id="form-produto-tabela-preco"]/div[3]/table/tbody/tr[3]/td[2]/input'
tam_G = '//*[@id="form-produto-tabela-preco"]/div[3]/table/tbody/tr[4]/td[2]/input'
tam_GG ='//*[@id="form-produto-tabela-preco"]/div[3]/table/tbody/tr[5]/td[2]/input'
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
    page.locator('//*[@id="main"]/nav/ul/li[5]/a/span').click()
    sleep(2)
    page.locator('//*[@id="main"]/nav/ul/li[5]/ul/li[2]/a').click()
    sleep(1)
    page.locator(atacado).click()
    sleep(0.5)
    page.locator('//*[@id="main"]/div[2]/div[3]/div[2]/a[2]').click()
    sleep(0.5)
    page.locator('//*[@id="s2id_IdProduto"]/a').click()
    sleep(0.7)
    page.locator('//*[@id="s2id_autogen2_search"]').fill(ref)
    sleep(0.5)
    page.keyboard.press("Enter")
    sleep(0.5)
    page.locator('//*[@id="form-produto-tabela-preco"]/div[2]/div[1]/div/div/span/button').click()
    sleep(0.5)
    page.fill(tam_P, valor)
    sleep(0.5)
    page.fill(tam_M, valor)
    sleep(0.5)
    page.fill(tam_G, valor)
    sleep(0.5)
    page.fill(tam_GG, valor)
    sleep(3)
    page.keyboard.press("Enter")
    sleep(10)