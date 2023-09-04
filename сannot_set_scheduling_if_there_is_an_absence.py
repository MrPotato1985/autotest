#ПРоверяем что при отсутсвии ты не можешь создать занятость


from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import funciones
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

try:
    #Авторизация

    link = "https://test.imredi.biz/admin" #ссылка на сайт

    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)

    #Ввод логина
    input1 = browser.find_element(By.ID, "id_username")
    input1.send_keys("andrew3")

    #Ввод пароля
    input2 = browser.find_element(By.ID, "id_password")
    input2.send_keys("qweasdzxc")

    #Нажатие на кнопку войти на сайт
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-info")
    button.click()

    #ПРОСТАВЛЯЕМ ОТСУТСВИЕ 

    #Нажимаем планирование графиков
    browser.find_element(By.LINK_TEXT, "Планирование графиков").click()
     
    #Нажимаем на Отсутствие сотрудников
    browser.find_element(By.LINK_TEXT, "Отсутствие сотрудников").click()

    #нажимаем на кнопку добавить отсутсвие сотрудника
    browser.find_element(By.CLASS_NAME, "btn.btn-success").click()
    
    #Заполняем фамилию сотрудника
    browser.find_element(By.ID, "select2-id_employee-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Баранов")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Добавляем дату начала отсутсвия
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    browser.find_element(By.ID, "id_start_date").send_keys(tomorrow.strftime("%d.%m.%Y"))

    #Добавляем дату окончания отсутсвия
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
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
    #browser.switch_to.alert.accept()

    #ПРОВЕРЯЕМ НЕВОЗМОЖНОСТЬ ДОБАВЛЕНИЯ СМЕНЫ ПЕРЕТАСКИВАНИЕМ
    
    #Нажимаем планирование графиков
    browser.find_element(By.LINK_TEXT, "Планирование графиков").click()
     
    #Нажимаем на планирование
    browser.find_element(By.LINK_TEXT, "Планирование").click()

    #нажимаем на одно из планирования
    browser.find_element(By.XPATH, "//a[contains(@href, '/admin/worktimeschedule/workplan/') and contains(@href, '/change')]").click()

    #переходим на новое окно
    browser.switch_to.window(browser.window_handles[1])

    link = browser.current_url + "#planing"
    
    #Нажимаем планирование графиков
    browser.find_element(By.LINK_TEXT, "Планирование графиков").click()
    

    browser.get(link)
                                                 
    WebDriverWait(browser, 40).until(presence_of_element_located((By.CSS_SELECTOR, "#calendar")))
    fio_element = browser.find_element(By.XPATH, "//div[starts-with(@id, 'user_48167')]") #впиши id юзера
    calendar_cells = browser.find_elements(By.CSS_SELECTOR, "td.fc-day")
    #calendar_cells = driver.find_elements(By.CSS_SELECTOR, "td.fc-day.fc-widget-content.fc-tue")

    # Используем ActionChains для drag-and-drop
    action_chains = ActionChains(browser)
    action_chains.click_and_hold(fio_element).perform()
    time.sleep(5)

    # Найдем координаты целевой ячейки и выполнием drop
    for cell in calendar_cells:
        if cell.get_attribute("data-date") == tomorrow.strftime("%Y-%m-%d"): #впиши дату для ячейки
            target_cell = cell
            break


    action_chains.move_to_element(target_cell).release().perform()

    #Нажимаем ок на всплывашке
    browser.switch_to.alert.accept()

    #ПРОВЕРЯЕМ НЕВОЗМОЖНОСТЬ ДОБАВЛЕНИЯ ЧЕРЕЗ ЗАНЯТОСТЬ ПО ДНЮ


    #Нажимаем планирование графиков
    browser.find_element(By.LINK_TEXT, "Планирование графиков").click()
     
    #Нажимаем на занятость по дням
    browser.find_element(By.LINK_TEXT, "Занятость по дням").click()

    #нажимаем на кнопку добавить занятость по дням
    browser.find_element(By.CLASS_NAME, "btn.btn-success").click()
    
    #Заполняем планирование
    browser.find_element(By.ID, "select2-id_plan-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Стофато")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Заполняем сотрудника в занятость по дням
    browser.find_element(By.ID, "select2-id_employee-container").click()
    browser.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Баранов")
    browser.find_element(By.CLASS_NAME, "select2-results__option.select2-results__option--highlighted").click()

    #Добавляем дату начала занятости
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    browser.find_element(By.ID, "id_start_time_0").send_keys(tomorrow.strftime("%d.%m.%Y"))

    #Добавляем время начала занятости
    browser.find_element(By.ID, "id_start_time_1").send_keys("5:00:00")

    #Добавляем дату окончания занятости
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    browser.find_element(By.ID, "id_end_time_0").send_keys(tomorrow.strftime("%d.%m.%Y"))

    #Добавляем время окончания занятости
    browser.find_element(By.ID, "id_end_time_1").send_keys("14:00:00")

    #Нажимаем на кнопку сохранить
    browser.find_element(By.CLASS_NAME, "btn.btn-high.btn-info").click()

    #Смотрим появилось ли сообщение об ошибке
    browser.find_element(By.CLASS_NAME, "alert.alert-error")


except:
    funciones.agregar_archivo("test.txt", "\n0 Тест не прошел")
    funciones.capture_screenshot()
else:
    funciones.agregar_archivo("test.txt", "\n1 Тест прошел успешно")



