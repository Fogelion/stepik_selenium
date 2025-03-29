from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys('firstname')
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys('lastname')
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys('email@mail.com')
    input4 = browser.find_element(By.CSS_SELECTOR, "#file")
    input4.send_keys(file_path)
    button1 = browser.find_element(By.CSS_SELECTOR, "form > button.btn.btn-primary")
    button1.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()