from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    button1 = browser.find_element(By.CSS_SELECTOR, ".container > button.trollface.btn.btn-primary")
    button1.click()
    # Имя новой вкладки
    new_window = browser.window_handles[1]
    # Имя текущей вкладки
    first_window = browser.window_handles[0]
    # Переключение на указанную вкладку
    browser.switch_to.window(new_window)


    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, ".container > button.btn.btn-primary")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()