#Удаление планирования
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
     
    #Нажимаем на планирование
    browser.find_element(By.LINK_TEXT, "Планирование").click()

    #Выбираем один из планов
    browser.find_element(By.NAME, "_selected_action").click()
    
    #Выбираем удалить
    select = Select(browser.find_element(By.NAME, "action"))
    select.select_by_value("delete_selected")
    
    #Нажимаем на кнопку удалить
    browser.find_element(By.XPATH, "//*[@id='changelist-form']/div[2]/button").click()

    #Подтверждение удаления
    browser.find_element(By.CLASS_NAME, "btn.btn-danger").click()

    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Удаление планирования не произошло")
    funciones.capture_screenshot()
else:
    funciones.agregar_archivo("test.txt", "\n1 Удаление планирования произошло")