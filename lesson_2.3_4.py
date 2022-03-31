#
# Glebezdin Artem
# lesson 2.3_4
# v1.0
#

import time
import math
from selenium.webdriver.common.by import By
from selenium import webdriver

# Ссылка на тестируемый продукт
link = "http://suninjuly.github.io/alert_accept.html"

try:
    # запускаем драйвер, передаем ссылку на продукт
    browser = webdriver.Chrome()
    browser.get(link)

    # Функция решающая уравнение в задаче
    def answer(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Нажимаем на первую кнопку
    button_1 = browser.find_element(By.CSS_SELECTOR, ".btn")
    button_1.click()

    # нажимаем ОК в модальном окне
    confirm = browser.switch_to.alert
    confirm.accept()
    # name = confirm.text  забираем текст из мадального окна
    # name.send_keys("My answer")  ввод данных в мадальное окно
    # confirm.dismiss()  Отмена

    # Забираем значение Х
    elem_x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = elem_x.text
    y = answer(x)

    # Вводим ответ в поле
    input_1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_1.send_keys(y)

    # Нажимаем на кнопку Submit
    button2 = browser.find_element(By.CSS_SELECTOR, ".btn")
    button2.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()