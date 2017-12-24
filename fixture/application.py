from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self, browser, base_url, login, password):
        if browser == 'firefox':
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        else:
            raise ValueError("Unrecognised browser %s" % browser)

#        self.wd.implicitly_wait(5) # useful when page is dynamically loaded
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url
        self.login = login
        self.password = password

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
