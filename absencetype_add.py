#Добавление типа отсутсвия
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
     
    #Нажимаем на занятость по дням
    browser.find_element(By.LINK_TEXT, "Отсутствие сотрудников").click()

    #нажимаем на кнопку  тип отсутсвия сотрудника
    browser.find_element(By.LINK_TEXT, "Типы отсутствий сотрудников").click()
    
    ##нажимаем на кнопку добавить тип отсутсвие 
    browser.find_element(By.CLASS_NAME, "btn.btn-success").click()
    
    #Заполняем код отсутсвия
    browser.find_element(By.ID, "id_absence_code").send_keys("001")

    #Заполняем метку отсутсвия
    browser.find_element(By.ID, "id_absence_label").send_keys("ОТГ")
    
    #Заполняем наименование отсутсвия
    browser.find_element(By.ID, "id_absence_name").send_keys("Отгул")

    #Заполняем тип отсутсвия
    select = Select(browser.find_element(By.ID, "id_absence_class"))
    select.select_by_value("1")
    
    #Нажимаем на кнопку сохранить
    browser.find_element(By.CLASS_NAME, "btn.btn-high.btn-info").click()

    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Тип отсутсвия не создался")
    funciones.capture_screenshot()
else:
    funciones.agregar_archivo("test.txt", "\n1 Тип отсутсвия создался")