#проверка что заяка не создается, если нет должности в штатном расписании и включена соответсвующая опция на подписчике

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
    browser.find_element(By.ID, "id_username").send_keys("andrew4")

    #Ввод пароля
    browser.find_element(By.ID, "id_password").send_keys("qweasdzxc")
    

    #Нажатие на кнопку войти на сайт
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-info").click()

    #Нажимаем на биржу смен
    browser.find_element(By.CLASS_NAME, "glyphicon.glyphicon-sort").click()
    #Нажимаем на Заявки на биржу
    browser.find_element(By.LINK_TEXT, "Заявки на Биржу").click()
    #Нажимаем на кнопку добавить заявку на биржу
    browser.find_element(By.CLASS_NAME, "icon-plus-sign.icon-white").click()


    #Добавляем точку
    point = browser.find_element(By.ID, "select2-id_point-container")
    point.click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Пушкина")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Добавляем должность
    browser.find_element(By.ID, "select2-id_position-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Дизайнер")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #добавляем должность
    browser.find_element(By.ID, "id_bid").send_keys("500")

    #Добавляем дату начала заявки
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=0)
    browser.find_element(By.ID, "id_start_date_0").send_keys(tomorrow.strftime("%d.%m.%Y"))

    now_time = now + datetime.timedelta(seconds=5)
    #Добавляем время начала заявки
    browser.find_element(By.ID, "id_start_date_1").send_keys(now_time.strftime("%H:%M:%S"))

    #Добавляем дату окончания заявки
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=0)
    browser.find_element(By.ID, "id_end_date_0").send_keys(tomorrow.strftime("%d.%m.%Y"))

    now_time = now + datetime.timedelta(seconds=30)
    #Добавляем время окончания заявки
    browser.find_element(By.ID, "id_end_date_1").send_keys(now_time.strftime("%H:%M:%S"))

    #Добавляем описания

    browser.find_element(By.ID, "id_description").send_keys("Это заявка создана вафлеботом")

    #нажимаем сохранить

    browser.find_element(By.NAME, "_save").click()

    #Если заявка создана пишем это в файл и наоборот. Смотрю по появлению алерта что заявка добавлена

    browser.find_element(By.CLASS_NAME, "errorlist.nonfield")
except:
    funciones.agregar_archivo("test.txt", "\n0 Что то пошло не так")
    funciones.capture_screenshot()
else:
    funciones.agregar_archivo("test.txt", "\n1 Заявка на биржу не создана так как нет должности")




