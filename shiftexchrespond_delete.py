#Удаление отклика с биржы

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

    #Нажимаем на биржу смен
    browser.find_element(By.CLASS_NAME, "glyphicon.glyphicon-sort").click()
    
    #Нажимаем на отлики по заявкам
    browser.find_element(By.LINK_TEXT, "Отклики на заявки в Бирже").click()

    #нажимаем на один из откликов
    browser.find_element(By.XPATH, "//a[contains(@href, '/admin/shiftexch/shiftexchrespond/') and contains(@href, '/change')]").click()

    #переходим на новое окно
    browser.switch_to.window(browser.window_handles[1])

    #нажимаем на кнопку удалить отклик
    browser.find_element(By.CLASS_NAME, "text-error.deletelink").click()
    
    #Подтверждаем удаление
    browser.find_element(By.CLASS_NAME, "btn.btn-danger").click()
    
    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Удаление отклика на биржу не произошло")
    funciones.capture_screenshot()
else:
    funciones.agregar_archivo("test.txt", "\n1 Удаление отклика на биржу произошло")