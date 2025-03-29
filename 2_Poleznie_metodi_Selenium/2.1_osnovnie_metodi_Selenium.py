from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    print("value x =", x)
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    button1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    button1.click()
    button2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    button2.click()
    button3 = browser.find_element(By.CSS_SELECTOR, "form > button.btn.btn-default")
    button3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()