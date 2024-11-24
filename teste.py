from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import json


#abre arquivo json
with open('values.json', 'r') as arquivo:
    dados = json.load(arquivo)

#abre o navegador
nav = webdriver.Chrome()

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

#clica no elemento
btnsim.click()

#busca o elemento que contenha 'Cadastro' no seu texto e em seguida move o mouse para sua posição 
#e faz a função "hover"
elecad = nav.find_element(by=By.XPATH, value="//a[contains(text(), 'Cadastro')]")
action.move_to_element(elecad).perform()

time.sleep(2)

#bucas pelo elemento que tenha "usuario" e clica no elemento
eleusu = nav.find_element(by=By.XPATH, value="//a[contains(text(), 'Usuário')]")
eleusu.click()

nav.quit()