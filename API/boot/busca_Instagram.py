from selenium import webdriver  #pip install selenium
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver_manager
import time

#Abre o Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com') #abre o instagram
time.sleep(15) # Tempo de espera'

s=['TESTE123']
# email: tt7839794
# senha teste123!

def usuario():                                                      
    campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
                                   
    time.sleep(5)
    campo_usuario.click()
    campo_usuario.send_keys("tt7839794")
    campo_usuario.send_keys(Keys.ENTER)
    
def senha():

    campo_senha = driver.find_element_by_xpath("//input[@name='password']")
    time.sleep(3)
    campo_senha.click()
    campo_senha.send_keys("teste123!")
    campo_senha.send_keys(Keys.ENTER)

def explorar():

    time.sleep(15)
    driver.get("https://www.instagram.com/explore/?next=%2F")
    time.sleep(10)
    driver.get("https://www.instagram.com/terceiroinfo3/?next=%2F")
    time.sleep(5)
    driver.get("https://www.instagram.com/p/Ch5Q-YPu6Jw/?next=%2F")
    time.sleep(10)
    driver.find_element_by_class_name("_aaoc").click()
    time.sleep(5)
    comentario  = driver.find_element_by_class_name("_aaoc")
    comentario.send_keys("O MORENO DE TERNO É GOSTOSO")
    comentario.send_keys(Keys.ENTER)

    # https://www.instagram.com/terceiroinfo3/?next=%2F
    #https://www.instagram.com/p/Ch5Q-YPu6Jw/?next=%2F

print("FOIIII")
usuario()
senha()
explorar()