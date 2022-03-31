#
# Glebezdin Artem
# lesson 1.6_7
# v1.0
#

from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Ссылка на тестируемый продукт
link = "http://suninjuly.github.io/huge_form.html"

try:
    # запускаем драйвер, передаем ссылку на продукт
    browser = webdriver.Chrome()
    browser.get(link)

    # Обозначаем поле для ввода информации
    elements = browser.find_elements(By.TAG_NAME, "input")

    # Передаем циклом слово "test" во все поля
    for element in elements:
        element.send_keys("test")

    # нажимаем кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
