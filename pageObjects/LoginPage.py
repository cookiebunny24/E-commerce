
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//input[@class='button-1 login-button']"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        ele = WebDriverWait(self.driver, 5000).until(
            EC.element_to_be_clickable(By.XPATH, self.button_login_xpath)
        )
        ele.click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

    def webdriverwait_with_xpath_clickable(self, element):
        wait=WebDriverWait(self.driver, 5000).until(
            EC.element_to_be_clickable(By.XPATH, element)
        )
