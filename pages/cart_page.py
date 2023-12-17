import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.utils import Utils


class Cart(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    ITEM_TEXT_FIELD = "//div[@class='_2-uG6-']/a"

    # Methods to get the fields
    def getItemTextField(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.ITEM_TEXT_FIELD)




