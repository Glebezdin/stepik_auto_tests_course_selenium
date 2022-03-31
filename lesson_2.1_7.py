#
# Glebezdin Artem
# lesson 2.1_7
# v1.0
#

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Ссылка на тестируемый продукт
link = "http://suninjuly.github.io/get_attribute.html"

try:
    # запускаем драйвер, передаем ссылку на продукт
    browser = webdriver.Chrome()
    browser.get(link)

    # Высчитываем значение X
    def zadacha(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Забираем значение из сундука и задаем переменную Х
    time.sleep(1)
    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
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
