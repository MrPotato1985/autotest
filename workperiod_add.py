#Добавление занятости по дням
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
     
    #Нажимаем на занятость по дням
    browser.find_element(By.LINK_TEXT, "Занятость по дням").click()

    #нажимаем на кнопку добавить занятость по дням
    browser.find_element(By.CLASS_NAME, "btn.btn-success").click()
    
    #Заполняем планирование
    browser.find_element(By.ID, "select2-id_plan-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("пушкина д. 4")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Заполняем сотрудника в занятость по дням
    browser.find_element(By.ID, "select2-id_employee-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Феськов")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Добавляем дату начала занятости
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=2)
    browser.find_element(By.ID, "id_start_time_0").send_keys(tomorrow.strftime("%d.%m.%Y"))

    #Добавляем время начала занятости
    browser.find_element(By.ID, "id_start_time_1").send_keys("5:00:00")

    #Добавляем дату окончания занятости
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=2)
    browser.find_element(By.ID, "id_end_time_0").send_keys(tomorrow.strftime("%d.%m.%Y"))

    #Добавляем время окончания занятости
    browser.find_element(By.ID, "id_end_time_1").send_keys("14:00:00")

    #Нажимаем на кнопку сохранить
    browser.find_element(By.CLASS_NAME, "btn.btn-high.btn-info").click()


    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Занятость по дням не создалась")
else:
    funciones.agregar_archivo("test.txt", "\n1 Занятость по дням создалась")