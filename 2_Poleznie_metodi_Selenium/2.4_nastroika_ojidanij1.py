from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "https://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # говорим Selenium проверять в течение 12 секунд, пока элемент не примет нужный вид'
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element ((By.ID, "price"), "$100")
    )
    button1 = browser.find_element(By.CSS_SELECTOR, "#book")
    button1.click()

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