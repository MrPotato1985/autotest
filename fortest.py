#Тест при проставлении отсутсвия заявка по которой был отклик в бирже не удаляеться из занятости по дням, время высвобождаеться, в занятости по дням проставляеться тип отсуствия


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
    input1.send_keys("andrew3")

    #Ввод пароля
    input2 = browser.find_element(By.ID, "id_password")
    input2.send_keys("qweasdzxc")

    #Нажатие на кнопку войти на сайт
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-info")
    button.click()

    
    #ПРОВЕРЯЕМ ЧТО ВРЕМЯ В ПЛАНИРОВАНИИ ВЫСВОБОДИЛОСЬ И РАВНО 0
    
    #Нажимаем планирование графиков
    browser.find_element(By.LINK_TEXT, "Планирование графиков").click()
     
    #Нажимаем на планирование
    browser.find_element(By.LINK_TEXT, "Планирование").click()

    #нажимаем на одно из планирования
    browser.find_element(By.XPATH, "//a[contains(@href, '/admin/worktimeschedule/workplan/') and contains(@href, '/change')]").click()

    #переходим на новое окно
    browser.switch_to.window(browser.window_handles[1])
                                                
    elem = browser.find_element(By.XPATH, '//*[@id="plan-stat-summary"]/div[4]/div[2]/span[1]')                                
    elem1 = int(elem.text)
    print(elem1)
    assert elem1 == 0  

    #ПРОВЕРЯЕМ ЧТО ПРОСТАВИЛСЯ ТИП ОТСУТСВИЯ В ЗАНЯТОСТИ ПО ДНЮ

    #Нажимаем планирование графиков
    browser.find_element(By.LINK_TEXT, "Планирование графиков").click()

    time.sleep(20) 
    
    #Нажимаем на занятость по дням
    browser.find_element(By.LINK_TEXT, "Занятость по дням").click()

    #Находи отгул и проверяем таким образом если он
    otgul = browser.find_element(By.LINK_TEXT, "Отгул")

    

    #Тест может не сработать так как тут фоновая и отгул может не появиться сразу ()

    
except:
    funciones.agregar_archivo("test.txt", "\n0 Тест не прошел")
    funciones.capture_screenshot()
else:
    funciones.agregar_archivo("test.txt", "\n1 Тест прошел успешно")



