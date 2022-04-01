#
# Glebezdin Artem
# lesson 3.6_3
# v1.0
#

import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    print("\nЗапуск браузера для теста!")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nЗавершение работы браузера!")
    browser.quit()


class TestAlienMessage():
    # Ссылки для задания
    links = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]

    # вызываем фикстуру, передаем в нее ссылки для задания
    @pytest.mark.parametrize('link', links)
    def test_guest_should_see_login_link(self, browser, link):
        browser.get(link)
        answer_time = str(math.log(int(time.time())))  # расчет ответа для input_1

        # Ожидаем загрузку поля ввода ответа / передаем в нее ответ
        input_1 = WebDriverWait(browser, 7).until(
            EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
        )
        input_1.send_keys(answer_time)

        # Ожидаем загрузку кнопки "Отправить" и нажимаем ее
        button_1 = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        button_1.click()

        # Считываем ответ от сервера и преобразуем его в текст
        answer_alien_1 = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".smart-hints__hint"))
        )
        answer_alien_2 = answer_alien_1.text
        answer_alien = answer_alien_2

        # производим сравнение ответа сервера с ожидаемым ответом
        assert answer_alien == "Correct!"




