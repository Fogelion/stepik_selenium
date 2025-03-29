from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x, y):
  return str(int(x) + int(y))

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_el = browser.find_element(By.CSS_SELECTOR, "#num1")
    num2_el = browser.find_element(By.CSS_SELECTOR, "#num2")
    num1 = num1_el.text
    num2 = num2_el.text
    res = calc(num1, num2)
    print(f"res: {num1} + {num2} = {res}")

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(res)  # ищем элемент с текстом "Python"
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button1.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()