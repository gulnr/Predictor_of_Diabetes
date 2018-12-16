from django.test import TestCase

# Create your tests here.
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from .models import User

class MySeleniumTests(StaticLiveServerTestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='group24',
                                             email='dummy@gmail.com',
                                             password='test123')

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver("C:\\Users\\eylul\\PycharmProjects\\irem_django2.1_aynisi\\chromedriver.exe")
        cls.selenium.implicitly_wait(10)



    def test1_login_success(self):
        #   login
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        time.sleep(1)
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('group24')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('test123')
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Log in')]")
        self.selenium.execute_script("arguments[0].click();", element)
        assert (self.selenium.find_element_by_xpath("//*[contains(@id, 'nav-username')]").text == self.user.username)
        time.sleep(2)

        #   change password
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Settings')]")
        self.selenium.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Change Password')]")
        self.selenium.execute_script("arguments[0].click();", element)
        time.sleep(1)
        old_password_input = self.selenium.find_element_by_name("old_password")
        old_password_input.send_keys("test123")
        time.sleep(1)
        new1_input = self.selenium.find_element_by_name("new_password1")
        new1_input.send_keys("pass123")
        time.sleep(1)
        new2_input = self.selenium.find_element_by_name("new_password2")
        new2_input.send_keys("pass123")
        time.sleep(1)
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Submit')]")
        self.selenium.execute_script("arguments[0].click();", element)
        time.sleep(1)

        #   logout
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Settings')]")
        self.selenium.execute_script("arguments[0].click();", element)
        time.sleep(2)
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Log out')]")
        self.selenium.execute_script("arguments[0].click();", element)
        time.sleep(1)

    def test2_login_fail(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('dummy')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('test123')
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Log in')]")
        self.selenium.execute_script("arguments[0].click();", element)
        username_input = self.selenium.find_element_by_name("username")
        username_input.clear()
        username_input.send_keys('group24')
        time.sleep(2)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('test12354')
        time.sleep(2)
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Log in')]")
        self.selenium.execute_script("arguments[0].click();", element)
        time.sleep(2)

        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Forget Password')]")
        self.selenium.execute_script("arguments[0].click();", element)
        time.sleep(1)
        email_input = self.selenium.find_element_by_id("id_email")
        email_input.send_keys('dummy@gmail.com')
        element = self.selenium.find_element_by_xpath("//*[contains(text(), 'Reset my password')]")
        #self.selenium.execute_script("arguments[0].click();", element)












