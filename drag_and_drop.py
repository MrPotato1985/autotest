from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

driver = webdriver.Chrome()

driver.get("https://test.imredi.biz/admin")

# Авторизация
username = driver.find_element(By.ID, "id_username")
password = driver.find_element(By.ID, "id_password")
login_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Войти"]')

username.send_keys("andrew") #впиши логин
password.send_keys("qweasdzxc") #впиши пароль
login_button.click()

driver.get("https://test.imredi.biz/admin/worktimeschedule/workplan/6811/change/#planing") #впиши путь

WebDriverWait(driver, 40).until(presence_of_element_located((By.CSS_SELECTOR, "#calendar")))
fio_element = driver.find_element(By.XPATH, "//div[starts-with(@id, 'user_5195')]") #впиши id юзера
calendar_cells = driver.find_elements(By.CSS_SELECTOR, "td.fc-day")
#calendar_cells = driver.find_elements(By.CSS_SELECTOR, "td.fc-day.fc-widget-content.fc-tue")

# Используем ActionChains для drag-and-drop
action_chains = ActionChains(driver)
action_chains.click_and_hold(fio_element).perform()
time.sleep(5)

# Найдем координаты целевой ячейки и выполнием drop
for cell in calendar_cells:
    if cell.get_attribute("data-date") == "2023-09-01": #впиши дату для ячейки
        target_cell = cell
        break

time.sleep(5)
action_chains.move_to_element(target_cell).release().perform()



# Задержка для просмотра результата
time.sleep(50)

