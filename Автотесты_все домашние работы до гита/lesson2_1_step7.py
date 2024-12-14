from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value_to_use = browser.find_element(By.TAG_NAME, "img")
    x = value_to_use.get_attribute("valuex")
    calculation = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calculation)
    
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()