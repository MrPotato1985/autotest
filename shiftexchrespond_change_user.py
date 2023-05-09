#Смена пользователя на отклие по заяки на биржу

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

    #нажимаем на кнопку изменить отклик
    browser.find_element(By.CLASS_NAME, "btn.btn-warning").click()
    
    #ищем нового пользователя
    browser.find_element(By.ID, "select2-id_user-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Стофато")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()
    
    #Добавляем причину изменения пользователя в отклике
    browser.find_element(By.ID, "id_user_change_reason").send_keys("Заболел")
    
    #нажимаем измнеить сотрудника
    browser.find_element(By.CLASS_NAME, "btn.btn-info").click()
    
    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Изменение сотрудника в отклике не произошло")
else:
    funciones.agregar_archivo("test.txt", "\n1 Изменение сотрудника в отклике произошло")