from pytests.support.hooks import *
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    # **
    # * Mapeamento de elementos
    # **

    @staticmethod
    def field_cpf(driver):
        return WebDriverWait(driver, 30).until(EC.visibility_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText')))

    @staticmethod
    def field_password(driver):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.EditText')))

    @staticmethod
    def button_entrar(driver):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]')))

    @staticmethod
    def invalid_user(driver):
        return WebDriverWait(driver, 30).until(EC.visibility_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView[1]')))

    # **
    # * Métodos e Funções hsauahsuahsuahsuhasuhaushaushaushaushaushaushauhsuahsuahsuahsuahsuahsuahsuahsuahsuahsuahsuahsuahus
    # **

    @staticmethod
    def login_screen(driver):
        LoginPage.field_cpf(driver)
        driver.save_screenshot(PATH_SCREENSHOT)

    @staticmethod
    def fill_login(driver, cpf, senha):
        LoginPage.field_cpf(driver).send_keys(cpf)
        LoginPage.field_password(driver).send_keys(senha)
        driver.save_screenshot(PATH_SCREENSHOT)

    @staticmethod
    def perform_login(driver):
        LoginPage.button_entrar(driver).click()
        LoginPage.invalid_user(driver)
        driver.save_screenshot(PATH_SCREENSHOT)
