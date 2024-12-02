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
time.sleep(3)

#busca os botões e campos 
usucod = nav.find_element(by=By.NAME, value="_USUCODC")
ususen = nav.find_element(by=By.NAME, value="_USUSEN")
btncon = nav.find_element(by=By.NAME, value="BUTTON1")

#limpa o campo e preenche em seguida
usucod.clear()
usucod.send_keys(dados['usucod'])

time.sleep(1)

#preenche o campo 
ususen.send_keys(dados['ususen'])

time.sleep(1)

#clica no botão para prosseguir
btncon.click()

#aguardar carregar a pagina
time.sleep(2)

#busca o elemento
btnsim = nav.find_element(by=By.NAME, value="BUTTON3")
if btnsim.is_displayed():
    #clica no elemento
    btnsim.click()


with open('devedores.json', 'r') as arqDevedores:
    arqDevedor = json.load(arqDevedores)
    devedores = arqDevedor.get('devedor','Erro')
    #codigos = devedores.get("codigo","Erro")

for codigo in devedores:
    navpes = nav.find_element(by=By.XPATH, value="//a[contains(text(), 'Pesquisar')]")
    action.move_to_element(navpes).perform()

    btnpes = nav.find_element(by=By.XPATH, value="//a[contains(text(), 'Pesquisar - Siscobra')]")
    btnpes.click()

    pesdevcod = nav.find_element(by=By.NAME, value="_DEVEDOR_CODIGO")
    pesdevcod.clear()
    pesdevcod.send_keys(codigo.values()) 

    btnpes = nav.find_element(by=By.NAME, value="BTN_PESQUISAR")
    btnpes.click()
    
    time.sleep(3)
    
    btndev = nav.find_element(by=By.ID, value='span__DEVCOD_0001')
    btndev.click()

    time.sleep(10)

    try:
        imagem = nav.find_element(By.XPATH, "//img[contains(@src, 'siscobra_topo.png')]")
        imagem.click()
    except Exception as e:
        print('imagem n encontrada')

siscfg = nav.find_element(By.XPATH, "//a[contains(text(), 'Siscobra Config')]")
action.move_to_element()

time.sleep(5)

nav.quit()