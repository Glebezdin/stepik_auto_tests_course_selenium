#
# Glebezdin Artem
# lesson 2.2_6
# v1.0
#

import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

# Ссылка на тестируемый продукт
link = "http://suninjuly.github.io/execute_script.html"

try:
    # запускаем драйвер, передаем ссылку на продукт
    browser = webdriver.Chrome()
    browser.get(link)

    # функция высчитывающая значение для Х.
    def answer(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # забираем значение примера
    elem_1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    elem_2 = elem_1.text
    x = elem_2
    y = answer(x)

    # скролим страницу, что-бы освободить кнопку от футера
    browser.execute_script("window.scrollBy(0, 200);")

    # вводим ответ в поле
    input_1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_1.send_keys(y)

    # выбор в checkbox "I'm the robot"
    checkbox_1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox_1.click()

    # выбор в radiobutton "Robots rule"
    radiobutton_1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton_1.click()

    # нажимаем кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
