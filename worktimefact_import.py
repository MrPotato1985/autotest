#Импорт фактически отработанного времени
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import funciones
import time 
import os

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
    #Нажимаем на фактически отработанного времени
    browser.find_element(By.LINK_TEXT, "Фактически отработанное время").click()

    #Нажимаем на Импорт
    browser.find_element(By.LINK_TEXT, "Импорт").click()
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'WorktimeFact_template.xlsx')
    
    #Добавляем файл
    browser.find_element(By.ID, "id_import_file").send_keys(file_path)

    #Нажимаем кнопку импорт
    browser.find_element(By.CLASS_NAME, "btn.btn-info").click()

    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Импорт ФРВ по ТТ не создалась")
    funciones.capture_screenshot()
else:
    funciones.agregar_archivo("test.txt", "\n1 Импорт ФРВ по ТТ создалась")