from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "https://suninjuly.github.io/selects1.html"
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element(By.ID, "num1")
    num1_val = int(num1.text)
    
    num2 = browser.find_element(By.ID, "num2")
    num2_val = int(num2.text)
    
    sum_nums = num1_val + num2_val
        
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum_nums))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()