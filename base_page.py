from selenium.webdriver.common.by import By
class BasePage:
    def __init__(self,driver,base_url='https://www.saucedemo.com/'):
        self.driver = driver
    def visit(self):
        return self.get('https://demoqa.com/')
    def find_element(self,locator):
        self.find_element(By.CSS_SELECTOR, 'locator')
