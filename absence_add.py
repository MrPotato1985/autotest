#Добавление отсутсвия
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
     
    #Нажимаем на Отсутствие сотрудников
    browser.find_element(By.LINK_TEXT, "Отсутствие сотрудников").click()

    #нажимаем на кнопку добавить отсутсвие сотрудника
    browser.find_element(By.CLASS_NAME, "btn.btn-success").click()
    
    #Заполняем фамилию сотрудника
    browser.find_element(By.ID, "select2-id_employee-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Феськов")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Добавляем дату начала отсутсвия
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=2)
    browser.find_element(By.ID, "id_start_date").send_keys(tomorrow.strftime("%d.%m.%Y"))

    #Добавляем дату окончания отсутсвия
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=2)
    browser.find_element(By.ID, "id_end_date").send_keys(tomorrow.strftime("%d.%m.%Y"))

    #Заполняем точку на которой было отсутсвие
    browser.find_element(By.ID, "select2-id_point-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Стофато")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Заполняем тип отсутсвия
    browser.find_element(By.ID, "select2-id_absence_type-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Отгул")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Нажимаем на кнопку сохранить
    browser.find_element(By.CLASS_NAME, "btn.btn-high.btn-info").click()

    #Нажимаем ок на всплывашке
    browser.switch_to.alert.accept()
   
    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Отсутсвие не создалось")
else:
    funciones.agregar_archivo("test.txt", "\n1 Отсутсвие создалось")