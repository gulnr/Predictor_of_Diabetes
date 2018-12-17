'''
To run test:
python manage.py test accounts.tests.MySeleniumTests
'''


from django.test import TestCase

# Create your tests here.
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
import time
import os
from .models import User
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class MySeleniumTests(StaticLiveServerTestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='group24',
                                             email='dummy@gmail.com',
                                             password='test123')

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        PROJECT_ROOT = os.path.abspath(os.path.dirname("irem_django2.1_aynisi"))
        cls.selenium = WebDriver(PROJECT_ROOT+"\\chromedriver.exe")
        cls.selenium.implicitly_wait(10)


    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):

        timeout = 2
        #   login
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('group24')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('test123')
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Log in')]")
        self.selenium.execute_script("arguments[0].click();", element)

        # Wait until the response is received
        WebDriverWait(self.selenium, timeout).until(
            lambda driver: driver.find_element_by_tag_name('body'))

        assert (self.selenium.find_element_by_xpath("//*[contains(@id, 'nav-username')]").text == self.user.username)

        timeout = 2
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Settings')]")
        self.selenium.execute_script("arguments[0].click();", element)
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Log out')]")
        self.selenium.execute_script("arguments[0].click();", element)

        # Wait until the response is received
        WebDriverWait(self.selenium, timeout).until(
            lambda driver: driver.find_element_by_xpath("//*[contains(text(), 'Log in')]"))

        # check the returned result
        assert 'Log in' in self.selenium.page_source


    def test_change_password(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('group24')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('test123')
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Log in')]")
        self.selenium.execute_script("arguments[0].click();", element)

        timeout=2
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Settings')]")
        self.selenium.execute_script("arguments[0].click();", element)

        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Change Password')]")
        self.selenium.execute_script("arguments[0].click();", element)

        old_password_input = self.selenium.find_element_by_name("old_password")
        old_password_input.send_keys("test123")

        new1_input = self.selenium.find_element_by_name("new_password1")
        new1_input.send_keys("pass1234")

        new2_input = self.selenium.find_element_by_name("new_password2")
        new2_input.send_keys("pass1234")

        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Submit')]")

        element.send_keys(Keys.RETURN)

        WebDriverWait(self.selenium, timeout).until(
            lambda driver: driver.find_element_by_tag_name('body'))

        assert 'Email' in self.selenium.page_source

        timeout = 2
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Settings')]")
        self.selenium.execute_script("arguments[0].click();", element)
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Log out')]")
        self.selenium.execute_script("arguments[0].click();", element)

        # Wait until the response is received
        WebDriverWait(self.selenium, timeout).until(
            lambda driver: driver.find_element_by_xpath("//*[contains(text(), 'Log in')]"))

        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('group24')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('pass1234')
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Log in')]")
        self.selenium.execute_script("arguments[0].click();", element)

        assert (self.selenium.find_element_by_xpath("//*[contains(@id, 'nav-username')]").text == self.user.username)


    def test_login_fail(self):

        timeout = 2
        #   login
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('group24')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('12345678545457875458787')
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Log in')]")
        self.selenium.execute_script("arguments[0].click();", element)

        # Wait until the response is received
        WebDriverWait(self.selenium, timeout).until(
            lambda driver: driver.find_element_by_tag_name('body'))

        assert "Please enter a correct username and password." in self.selenium.page_source

