#Добавление планирования
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import funciones
import time 

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

    #нажимаем на кнопку добавить график
    browser.find_element(By.CLASS_NAME, "btn.btn-success").click()
    
    #Заполняем режим
    browser.find_element(By.ID, "select2-id_point-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("пушкина д. 4")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Нажимаем на кнопку создать
    browser.find_element(By.CLASS_NAME, "btn.btn-info").click()

    #Нажимаем на кнопку сохранить
    browser.find_element(By.CLASS_NAME, "btn.btn-high.btn-info").click()


    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Планирование не добавлено")
else:
    funciones.agregar_archivo("test.txt", "\n1 Планирование добавлено")