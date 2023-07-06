from pytests.support.hooks import *
from selenium.webdriver.support import expected_conditions as EC
from pytests.pages.login_page import LoginPage
import allure

@pytest.mark.test_login_sucesso
def test_login(driver):
    with allure.step("acessar o app"):
        LoginPage.login_screen(driver)
        allure.attach.file(PATH_SCREENSHOT, attachment_type=allure.attachment_type.PNG)
    with allure.step("preencher os campos de login"):
        LoginPage.fill_login(driver, "40065661826", "Valido123@")
        allure.attach.file(PATH_SCREENSHOT, attachment_type=allure.attachment_type.PNG)
    with allure.step("Realizaro login"):
        LoginPage.perform_login(driver)
        allure.attach.file(PATH_SCREENSHOT, attachment_type=allure.attachment_type.PNG)
