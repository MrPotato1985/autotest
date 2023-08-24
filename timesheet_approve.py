#Утверждение табеля
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import funciones
import time 
import os
from selenium.webdriver.support.ui import Select

try:
    #Авторизация

    link = "https://test.imredi.biz/admin" #ссылка на сайт

    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)

    #Ввод логина
    input1 = browser.find_element(By.ID, "id_username")
    input1.send_keys("andrew2")

    #Ввод пароля
    input2 = browser.find_element(By.ID, "id_password")
    input2.send_keys("qweasdzxc")

    #Нажатие на кнопку войти на сайт
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-info")
    button.click()

    #Учёт рабочего времени
    browser.find_element(By.LINK_TEXT, "Учёт рабочего времени").click()
    #Нажимаем на табель
    browser.find_element(By.LINK_TEXT, "Табель").click()

    #Нажимаем на запись чекбох
    browser.find_element(By.CLASS_NAME, "action-select").click()
                                          
    #Выбераем в селектах утверждение  
    select = Select(browser.find_element(By.NAME, "action"))    
    select.select_by_value("approve_action")
   
    #нажимаем Утвердить
    browser.find_element(By.NAME, "index").click()

    #Нажимаем на запись чекбох
    elem = browser.find_element(By.XPATH, '//*[@id="result_list"]/tbody/tr/td[14]/img')
    assert(elem.get_attribute("alt") == "True")  
    
except:
    funciones.agregar_archivo("test.txt", "\n0 Утверждение табеля не создалось")
    funciones.capture_screenshot()
else:
    funciones.agregar_archivo("test.txt", "\n1 Утверждение табеля создалось")