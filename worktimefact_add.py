#Добавление фактически отработанного времени

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

    #Учёт рабочего времени
    browser.find_element(By.LINK_TEXT, "Учёт рабочего времени").click()
    #Нажимаем на фактически отработанного времени
    browser.find_element(By.LINK_TEXT, "Фактически отработанное время").click()
    
    #Нажимаем на кнопку фактически отработанное время
    browser.find_element(By.CLASS_NAME, "btn.btn-success").click()

    #Добавляем сотрудника
    browser.find_element(By.ID, "select2-id_user-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Феськов")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Добавляем точку
    point = browser.find_element(By.ID, "select2-id_point-container")
    point.click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Стофато")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Добавляем дату фактического времени
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=-1)
    browser.find_element(By.ID, "id_start_time_0").send_keys(tomorrow.strftime("%d.%m.%Y"))

    
    #Добавляем время начала заявки
    browser.find_element(By.ID, "id_start_time_1").send_keys("09:00:00")

    #Добавляем дату окончания заявки
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=-1)
    browser.find_element(By.ID, "id_end_time_0").send_keys(tomorrow.strftime("%d.%m.%Y"))

    
    #Добавляем время окончания заявки
    browser.find_element(By.ID, "id_end_time_1").send_keys("18:00:00")

    
    #нажимаем сохранить
    browser.find_element(By.NAME, "_save").click()

    #Если факт не создан пишем это в файл и наоборот. Смотрю по появлению алерта что заявка добавлена

    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Фактически отработанное время не создано")
    funciones.capture_screenshot()
else:
    funciones.agregar_archivo("test.txt", "\n1 Фактически отработанное время создано")




