#
# Glebezdin Artem
# lesson 2.1_5
# v1.0
#

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Ссылка на тестируемый продукт
link = "http://suninjuly.github.io/math.html"

try:
    # запускаем драйвер, передаем ссылку на продукт
    browser = webdriver.Chrome()
    browser.get(link)

    # Высчитываем значение X
    def zadacha(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    time.sleep(1)
    # выбираем текст и задаем переменную х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = zadacha(x)

    # Вводим значение
    input_1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_1.send_keys(y)

    # выбор в checkbox "I'm the robot"
    checkbox_1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox_1.click()

    # выбор в radiobutton "Robots rule"
    radiobutton_1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton_1.click()

    time.sleep(1)
    # нажимаем кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
