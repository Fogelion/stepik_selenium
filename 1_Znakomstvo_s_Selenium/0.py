
# from gigachat

from selenium import webdriver

# Создаем объект веб-драйвера
driver = webdriver.Chrome()

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By



# from https://www.selenium.dev/documentation/webdriver/getting_started/first_script/

# Переходим на сайт
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Запросить информацию о браузере
title = driver.title

# Определить стратегию ожидания
driver.implicitly_wait(0.5)

# Найдите элемент
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# Принять меры по элементу
text_box.send_keys("Selenium")
submit_button.click()

# Запрос информации об элементе
message = driver.find_element(by=By.ID, value="message")
text = message.text

# Завершить сеанс
driver.quit()













