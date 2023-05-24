#Добавление ФРВ по ТТ
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
     
    #Нажимаем на ФРВ по ТТ
    browser.find_element(By.LINK_TEXT, "ФРВ по ТТ").click()

    #нажимаем на кнопку добавить ФРВ по ТТ
    browser.find_element(By.CLASS_NAME, "btn.btn-success").click()
    
    #Заполняем точку
    browser.find_element(By.ID, "select2-id_point-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Пушкина д. 3")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Добавляем дату месяц
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=0)
    browser.find_element(By.ID, "id_month").send_keys(tomorrow.strftime("%d.%m.%Y"))

    #Заполняем часы
    browser.find_element(By.ID, "id_hours").send_keys("60")

    #Нажимаем на кнопку сохранить
    browser.find_element(By.CLASS_NAME, "btn.btn-high.btn-info").click()
     
    #Нажимаем на планирование
    browser.find_element(By.LINK_TEXT, "Планирование").click()
     
    #нажимаем на одно из планирования
    browser.find_element(By.XPATH, "//a[contains(@href, '/admin/worktimeschedule/workplan/') and contains(@href, '/change')]").click()

    #переходим на новое окно
    browser.switch_to.window(browser.window_handles[1])

    #смотрим появилось ли в планировании резерв по ФРВ
    browser.find_element(By.CLASS_NAME, "stat-item.item-reserve")
except:
    funciones.agregar_archivo("test.txt", "\n0 ФРВ по ТТ не создалось")
else:
    funciones.agregar_archivo("test.txt", "\n1 ФРВ по ТТ создалось")