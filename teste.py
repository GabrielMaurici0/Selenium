from selenium import webdriver
from selenium.webdriver.common.by import By
import time

nav = webdriver.Chrome()

nav.get("https://www.moozcobranca.com.br/homologacao/servlet/hsiscobra")

time.sleep(3)

usucod = nav.find_element(by=By.NAME, value="_USUCODC")
ususen = nav.find_element(by=By.NAME, value="_USUSEN")
btncon = nav.find_element(by=By.NAME, value="BUTTON1")

time.sleep(3)


usucod.clear()
usucod.send_keys("09541215971")

time.sleep(5)

ususen.send_keys("S#$0#uXE)0uYq9V4m2+_")

# time.sleep(2)

#btncon.click()


time.sleep(50000)
