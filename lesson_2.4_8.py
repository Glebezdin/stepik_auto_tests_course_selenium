#
# Glebezdin Artem
# lesson 2.2_6
# v1.0
#

import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    # запускаем драйвер, передаем ссылку на продукт
    browser = webdriver.Chrome()
    browser.get(link)

    # функция высчитывающая значение для Х.
    def answer(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # ожидаем когда цена достигнет 100$ и нажимаем кнопку
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))  # Задаем счетчик ожидания
    button1 = browser.find_element(By.ID, "book")  # Объявляем кнопку
    button1.click()

    # скрол страницы на 500px
    browser.execute_script("window.scrollBy(0, 600);")

    # Забираем значение Х
    elem_x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = elem_x.text
    y = answer(x)

    # Вводим ответ в поле
    input_1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_1.send_keys(y)

    # Нажимаем на кнопку Submit
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()