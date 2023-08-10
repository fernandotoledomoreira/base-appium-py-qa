import allure
from pytests.support.hooks import *

class ScreenshotService:

    def take_screenshot(driver):
        driver.save_screenshot(os.environ['PATH_SCREENSHOT'])
        allure.attach.file(os.environ['PATH_SCREENSHOT'], attachment_type=allure.attachment_type.PNG)