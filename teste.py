from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import random
from selenium.webdriver.common.keys import Keys

#abre arquivo json
with open('values.json', 'r') as arquivo:
    dados = json.load(arquivo)

#abre o navegador
nav = webdriver.Chrome()

nav.set_window_size(1920, 1080)

#criação obj ActionChains
action = ActionChains(nav)

#após abrir o navegador vai para a url
nav.get(dados['url'])

#espera a pagina carregar
time.sleep(2)

#busca os botões e campos 
usucod = nav.find_element(by=By.NAME, value="_USUCODC")
ususen = nav.find_element(by=By.NAME, value="_USUSEN")
btncon = nav.find_element(by=By.NAME, value="BUTTON1")

#limpa o campo e preenche em seguida
usucod.clear()
usucod.send_keys(dados['usucod'])

#preenche o campo 
ususen.send_keys(dados['ususen'])

#clica no botão para prosseguir
btncon.click()

#aguardar carregar a pagina
time.sleep(2)

#busca o elemento
btnsim = nav.find_element(by=By.NAME, value="BUTTON3")

if btnsim.is_displayed():
    #clica no elemento
    btnsim.click()

time.sleep(10)
"""
elemento = nav.find_element(By.TAG_NAME, value="body")

largura_tela = nav.execute_script("return window.innerWidth")
altura_tela = nav.execute_script("return window.innerHeight")
x_aleatorio = random.randint(0, largura_tela)
y_aleatorio = random.randint(0, altura_tela)

action.key_down(Keys.SHIFT).send_keys(Keys.PRINT_SCREEN).key_up(Keys.SHIFT).key_up(Keys.PRINT_SCREEN).perform()

action.move_to_element(elemento).move_by_offset(x_aleatorio, y_aleatorio).click().perform()

time.sleep(10)

action.key_down(Keys.SHIFT).send_keys(Keys.PRINT_SCREEN).key_up(Keys.SHIFT).key_up(Keys.PRINT_SCREEN).perform()

"""
nav.quit()