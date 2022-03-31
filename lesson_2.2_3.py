#
# Glebezdin Artem
# lesson 2.2_3
# v1.0
#

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# ссылки для тестов
link_1 = "http://suninjuly.github.io/selects1.html"
link_2 = "http://suninjuly.github.io/selects2.html"

try:
    # запускаем драйвер, передаем ссылку на продукт
    browser = webdriver.Chrome()
    browser.get(link_1)

    # Функция для получения значения
    def answer(num_1, num_2):
        return int(int(num_1) + int(num_2))

    # Забираем значения примера
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    num_1 = num1.text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    num_2 = num2.text
    num4 = answer(num_1, num_2)
    str(num4)

    # Выбор необходимого значения в списке
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_visible_text("%s" %num4)

    # нажимаем кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
