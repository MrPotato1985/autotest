#Добавление журнала рабочего времени
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
    #Нажимаем на Журнал учета рабочего времени
    browser.find_element(By.LINK_TEXT, "Журнал учета рабочего времени").click()
    
    #Нажимаем на кнопку добавить журнал учета рабочего времени
    browser.find_element(By.CLASS_NAME, "btn.btn-success").click()

    #Добавляем сотрудника
    browser.find_element(By.ID, "select2-id_user-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Феськов")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Добавляем точку
    browser.find_element(By.ID, "select2-id_point-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Стофато")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Добавляем дату прихода
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=-1)
    browser.find_element(By.ID, "id_income_last_update_0").send_keys(tomorrow.strftime("%d.%m.%Y"))

    
    #Добавляем время прихоода
    browser.find_element(By.ID, "id_income_last_update_1").send_keys("09:00:00")

    #Добавляем дату ухода
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=-1)
    browser.find_element(By.ID, "id_outcome_last_update_0").send_keys(tomorrow.strftime("%d.%m.%Y"))

    
    #Добавляем время ухода
    browser.find_element(By.ID, "id_outcome_last_update_1").send_keys("18:00:00")

    
    #нажимаем сохранить
    browser.find_element(By.NAME, "_save").click()

    #Если журнал учета не создан пишем это в файл и наоборот. Смотрю по появлению алерта что заявка добавлена

    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Добавление журнала рабочего времени не произошло")
    funciones.capture_screenshot()
else:
    funciones.agregar_archivo("test.txt", "\n1 Добавление журнала рабочего времени произошло")




