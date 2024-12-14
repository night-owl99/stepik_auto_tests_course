from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Ждём, пока цена не станет 100 долларов
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    
    # Жмем кнопку
    button = browser.find_element(By.ID, "book")
    button.click()
    
    # решаем пример
    num1 = browser.find_element(By.ID, "input_value")
    num1_val = math.log(abs(12*math.sin(int(num1.text))))
        
    input = browser.find_element(By.ID, "answer")
    input.send_keys(str(num1_val))
    
    # Жмем Submit
    button = browser.find_element(By.ID, "solve")
    button.click()
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()