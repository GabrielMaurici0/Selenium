from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

with open('values.json', 'r') as arquivo:
    dados = json.load(arquivo)

nav = webdriver.Chrome()

nav.get(dados['url'])

time.sleep(3)

usucod = nav.find_element(by=By.NAME, value="_USUCODC")
ususen = nav.find_element(by=By.NAME, value="_USUSEN")
btncon = nav.find_element(by=By.NAME, value="BUTTON1")

time.sleep(3)


usucod.clear()
usucod.send_keys(dados['usucod'])

time.sleep(5)

ususen.send_keys(dados['ususen'])

# time.sleep(2)

#btncon.click()


time.sleep(50000)
