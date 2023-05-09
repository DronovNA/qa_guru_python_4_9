import allure
from selene import by, be
from selene import browser


def test_open_start_page():
    with allure.step("Открываем главую страницу GitHub"):
        browser.open_url("https://github.com")

    with allure.step("Ищем репозиторий"):
        browser.element(".header-search-input").click()
        browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
        browser.element(".header-search-input").submit()

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 76"):
        browser.element(by.partial_text("#76")).should(be.visible)