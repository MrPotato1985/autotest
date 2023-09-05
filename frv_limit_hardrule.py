#Проверяем правило "Жесткий лимит ФРВ" при превышении нельзя утвердть график


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
    input1.send_keys("dd@imredi.biz8")

    #Ввод пароля
    input2 = browser.find_element(By.ID, "id_password")
    input2.send_keys("qweasdzxc")

    #Нажатие на кнопку войти на сайт
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-info")
    button.click()

    # ДОБАВЛЯЕМ СМЕНУ ПЕРЕТАСКИВАНИЕМ ЧТОБЫ БЫЛ ПЕРЕЛЕМИТ
    
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
    
    #Получаем дату
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)

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

    time.sleep(3)

    #смотрим предупреждение о превышении лимита
    browser.find_elements(By.CSS_SELECTOR, "alert.imredi-alert.alert-warning")

    #смотрим что нельзя нажать кнопку
    confirm = browser.find_element(By.ID, "calendar-confirm")
    assert confirm.get_attribute("disabled")
    


except:
    funciones.agregar_archivo("test.txt", "\n0 Тест не прошел")
    funciones.capture_screenshot()
else:
    funciones.agregar_archivo("test.txt", "\n1 Тест прошел успешно")



