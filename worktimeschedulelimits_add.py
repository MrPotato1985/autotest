#Добавление правила и ограничения
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import funciones
import time 
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

    #Нажимаем планирование графиков
    browser.find_element(By.LINK_TEXT, "Планирование графиков").click()
     
    #Нажимаем на Правила и ограничения
    browser.find_element(By.LINK_TEXT, "Правила и ограничения").click()

    #нажимаем на кнопку добавить Правила и ограничения
    browser.find_element(By.CLASS_NAME, "btn.btn-success").click()
    
    #Добавляем название ограничения
    browser.find_element(By.ID, "id_name").send_keys("Переработка в течении месяца")
    
    #Добавляем правило
    select = Select(browser.find_element(By.ID, "id_rule"))
    select.select_by_value("4")

    #Добавляем значение
    browser.find_element(By.ID, "id_value").send_keys("10")

    #Добавляем правило
    Select(browser.find_element(By.ID, "id_unit")).select_by_value("2")

    #Добавляем тип ограничения
    Select(browser.find_element(By.ID, "id_type_of_limit")).select_by_value("1")

    #Добавляем тип правила
    Select(browser.find_element(By.ID, "id_type_of_rule")).select_by_value("1")
    
    #нажимаем на кнопку сохранить
    browser.find_element(By.CLASS_NAME, "btn.btn-high.btn-info").click()
    
    
    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Правила и ограничения не создался")
else:
    funciones.agregar_archivo("test.txt", "\n1 Правила и ограничения создался")