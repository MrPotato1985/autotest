#Добавление типа присутсвия
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
     
    #Нажимаем на Типы присутствий сотрудников
    browser.find_element(By.LINK_TEXT, "Типы присутствий сотрудников").click()

    #нажимаем на кнопку добавить добавить тип присутсвия
    browser.find_element(By.CLASS_NAME, "btn.btn-success").click()
    
    #Заполняем код присутсвия
    browser.find_element(By.ID, "id_presence_code").send_keys("СВ")
    
    #Заполняем название присутсвия
    browser.find_element(By.ID, "id_presence_name").send_keys("Сверхуроч")
    
    #Заполняем метку присутсвия
    browser.find_element(By.ID, "id_presence_label").send_keys("СВ")

    select = Select(browser.find_element(By.ID, "id_presence_class"))
    select.select_by_value("4")
    
    #Ставим галочку основной тип для присутсвия
    browser.find_element(By.ID, "id_is_main").click()

    #Нажимаем на кнопку сохранить
    browser.find_element(By.CLASS_NAME, "btn.btn-high.btn-info").click()
   
    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Тип отсутсвия не создалось")
    funciones.capture_screenshot()
else:
    funciones.agregar_archivo("test.txt", "\n1 Тип отсутсвия создалось")