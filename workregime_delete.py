#Удаление режима работы
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
     
    #Нажимаем на режим работы
    browser.find_element(By.LINK_TEXT, "Режимы работы").click()

    #нажимаем на один из откликов
    browser.find_element(By.XPATH, "//a[contains(@href, '/admin/user/workregime/') and contains(@href, '/change')]").click()

    #переходим на новое окно
    browser.switch_to.window(browser.window_handles[1])

    #нажимаем на кнопку удалить режим
    browser.find_element(By.CLASS_NAME, "text-error.deletelink").click()
    
    #Подтверждаем удаление
    browser.find_element(By.CLASS_NAME, "btn.btn-danger").click()
    
    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Режим работы не удалился")
else:
    funciones.agregar_archivo("test.txt", "\n1 Режим работы удалился")