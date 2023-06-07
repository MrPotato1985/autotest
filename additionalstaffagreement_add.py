#Добавление Доп. часы по ТТ
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
     
    #Нажимаем на Доп. часы по ТТ
    browser.find_element(By.LINK_TEXT, "Доп. часы по ТТ").click()

    #нажимаем на кнопку добавить Доп. часы по ТТ
    browser.find_element(By.CLASS_NAME, "btn.btn-success").click()
    
    #Добавляем точку
    browser.find_element(By.ID, "select2-id_point-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Стофато")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Добавляем дату 
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=0)
    browser.find_element(By.ID, "id_month").send_keys(tomorrow.strftime("%d.%m.%Y"))

    #Добавляем часы
    browser.find_element(By.ID, "id_hours").send_keys("8")

    #Добавляем сумму
    browser.find_element(By.ID, "id_amount").send_keys("10000")
    
    #нажимаем на кнопку сохранить
    browser.find_element(By.CLASS_NAME, "btn.btn-high.btn-info").click()
    
    
    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Доп. часы по ТТ не создался")
    funciones.capture_screenshot()
else:
    funciones.agregar_archivo("test.txt", "\n1 Доп. часы по ТТ создался")