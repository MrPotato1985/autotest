#Откликнуться на заяку с биржу

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
    #Нажимаем на Заявки на биржу
    browser.find_element(By.LINK_TEXT, "Заявки на Биржу").click()

    #нажимаем на одну из заявок
    browser.find_element(By.XPATH, "//a[contains(@href, '/admin/shiftexch/shiftexchrequest/') and contains(@href, '/change')]").click()

    #переходим на новое окно
    browser.switch_to.window(browser.window_handles[1])

    #Нажимафем на кнопку отклинкться
    browser.find_element(By.CLASS_NAME, "btn.btn-info").click()

    #Нажимаем на кнопку подтверждения отклика "Да я уверен"
    browser.find_element(By.CLASS_NAME, "btn.btn-danger").click()

    #Если отклик успешен пишем это в файл и наоборот. Смотрю по появлению алерта что отклик добавлен

    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Отклик на биржу не создался")
    funciones.capture_screenshot()
else:
    funciones.agregar_archivo("test.txt", "\n1 Откли на биржу успешно создался")



