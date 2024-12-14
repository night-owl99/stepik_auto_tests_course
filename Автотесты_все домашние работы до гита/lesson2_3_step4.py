from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import math

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Жмем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()
    
    # свитч на алерт, принимаем его
    alert = browser.switch_to.alert
    alert.accept()
    
    # решаем пример
    num1 = browser.find_element(By.ID, "input_value")
    num1_val = math.log(abs(12*math.sin(int(num1.text))))
        
    input = browser.find_element(By.ID, "answer")
    input.send_keys(str(num1_val))
    
    # Жмем Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()