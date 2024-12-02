from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
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

if btnsim.is_displayed():
    #clica no elemento
    btnsim.click()



menreg = nav.find_element(by=By.XPATH, value="//a[contains(text(), 'Regras')]")
action.move_to_element(menreg).perform()

time.sleep(2)

menproaut = nav.find_element(by=By.XPATH, value="//a[contains(text(), 'Processos Automaticos')]")
menproaut.click()

proautseq = nav.find_element(by=By.NAME, value='PROAUTSEQ')

proautseq.clear()
proautseq.send_keys('1050')

btnproaut = nav.find_element(by=By.NAME, value='BTN_GET')
btnproaut.click()

btnexe = nav.find_element(by=By.NAME, value="BTNEXECUTAR")
#btnexe.click()

proautseq = nav.find_element(by=By.NAME, value='PROAUTSEQ')

proautseq.clear()
proautseq.send_keys('1051')

btnproaut = nav.find_element(by=By.NAME, value='BTN_GET')
btnproaut.click()

btnexe = nav.find_element(by=By.NAME, value="BTNEXECUTAR")
#btnexe.click()

time.sleep(2)

btnopc = nav.find_element(by=By.XPATH, value="//a[contains(text(), 'Opções')]")
action.move_to_element(btnopc).perform()        

recarq = nav.find_element(by=By.XPATH, value="//a[contains(text(), 'Recuperação de Arquivos')]")
recarq.click()

datrem = nav.find_element(by=By.NAME, value="_BORDATREMINI")
datrem.clear()
datrem.send_keys('28/11/2024')

time.sleep(3)

trocaTipo = nav.find_element(by=By.NAME, value="_BORTIP")
trocaTipo.click()

time.sleep(3)

trocaTipo2 = nav.find_element(by=By.XPATH, value="//a[contains(text(), 'Negativação')]")
trocaTipo2.click()

btncon = nav.find_element(by=By.NAME, value="BTNENTER")
btncon.click()

time.sleep(500)


nav.quit()