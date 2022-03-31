#
# Glebezdin Artem
# lesson 2.2_8
# v1.0
#

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Ссылка на тестируемый продукт
link = "http://suninjuly.github.io/file_input.html"

try:
    # запускаем драйвер, передаем ссылку на продукт
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    # Заполняем поля регистрации, тестовой информацией
    input_1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input_1.send_keys("Artem")
    input_2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input_2.send_keys("Ivanov")
    input_3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input_3.send_keys("test@test.ru")

    # Прикрепляем файл к форме регистрации
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'new2.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")  # находим элемент для загрузки файла
    element.send_keys(file_path)  # передаем путь файла

    # нажимаем кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()