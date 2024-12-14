from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.CSS_SELECTOR, "[name = 'lastname']")
    input1.send_keys('Петя')
    
    input2 = browser.find_element(By.CSS_SELECTOR, "[name = 'firstname']")
    input2.send_keys('Петьков')
    
    input3 = browser.find_element(By.CSS_SELECTOR, "[name = 'email']")
    input3.send_keys('kuzkinmat@yandgrr.com')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    
    file = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()