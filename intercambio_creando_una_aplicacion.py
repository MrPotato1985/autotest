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
    input1.send_keys("andrew")

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
    #Нажимаем на кнопку добавить заявку на биржу
    browser.find_element(By.CLASS_NAME, "icon-plus-sign.icon-white").click()


    #Добавляем точку
    point = browser.find_element(By.ID, "select2-id_point-container")
    point.click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Стофато")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Добавляем должность
    browser.find_element(By.ID, "select2-id_position-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Дизайнер")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()


    #Добавляем должность
    browser.find_element(By.ID, "select2-id_position-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Дизайнер")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Добавляем дату начала заявки

    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    browser.find_element(By.ID, "id_start_date_0").send_keys(tomorrow.strftime("%d.%m.%Y"))

    #Добавляем время начала заявки

    browser.find_element(By.ID, "id_start_date_1").send_keys("14:00:00")

    #Добавляем дату окончания заявки

    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    browser.find_element(By.ID, "id_end_date_0").send_keys(tomorrow.strftime("%d.%m.%Y"))

    #Добавляем время окончания заявки

    browser.find_element(By.ID, "id_end_date_1").send_keys("14:30:00")

    #Добавляем описания

    browser.find_element(By.ID, "id_description").send_keys("Это заявка создана вафлеботом")

    #нажимаем сохранить

    browser.find_element(By.NAME, "_save").click()

    #Если заявка создана пишем это в файл и наоборот. Смотрю по появлению алерта что заявка добавлена

    browser.find_element(By.CLASS_NAME, "alert.alert-success")
except:
    funciones.agregar_archivo("test.txt", "\n0 Заявка на биржу не создана")
else:
    funciones.agregar_archivo("test.txt", "\n1 Заявка на биржу успешно создана")




