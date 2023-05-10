import allure
from allure_commons.types import Severity
from selene import by, be
from selene import browser


url = "https://github.com"
repository = "eroshenkoam/allure-example"
issue_num = "#76"


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Dronov')
@allure.feature(f'Проверка наличия Issue {issue_num}')
@allure.story('Шаги с декоратором @allure.step')
@allure.link(url, name='Test')

def test_decorator_steps():
    open_main_page(url)
    search_for_repository(repository)
    go_to_repository(repository)
    open_issue_tab()
    should_see_issue_with_number(issue_num)


@allure.step("Открываем главную страницу")
def open_main_page(url):
    browser.open(url)


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys(repo)
    browser.element(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text("eroshenkoam/allure-example")).click()

@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()

@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text("#76")).should(be.visible)