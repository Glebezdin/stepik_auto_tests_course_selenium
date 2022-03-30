import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


# Ссылка на тестируемый продукт
link = "http://suninjuly.github.io/find_link_text"

try:
    # запускаем драйвер, передаем ссылку на продукт
    browser = webdriver.Chrome()
    browser.get(link)

    # Расчет искомого значения
    math_number = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    # Поиск значения в списке
    search_number = browser.find_element(By.LINK_TEXT, math_number)
    search_number.click()

    # заполняем форму регистрации тестовыми данными
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "firstname")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    # нажимаем кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
