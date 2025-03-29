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

    chest = browser.find_element(By.ID, "treasure")
    value_x = chest.get_attribute("valuex")
    print("value x =", value_x)
    y = calc(value_x)
    print("secret =", y)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    button1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    button1.click()
    button2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    button2.click()
    button3 = browser.find_element(By.CSS_SELECTOR, ".form-group > div > button.btn.btn-default")
    button3.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()