#
# Glebezdin Artem
# lesson 1.6_8
# v1.0
#

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Ссылка на тестируемый продукт
link = "http://suninjuly.github.io/find_xpath_form"

try:
    # запускаем драйвер, передаем ссылку на продукт
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем форму регистрации тестовыми данными
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "firstname")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    # нажимаем кнопку "Submit" используя Xpath путь
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
