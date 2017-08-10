import time
from selenium import webdriver

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, **options):
        print("\nRuning Selenium Tests..!")
        self.driver = webdriver.Chrome('/Users/ashik/Desktop/chromedriver')
        self.driver.get('%s%s' % ('http://127.0.0.1:8000', '/admin/'))
        username_field = self.driver.find_element_by_name("username")
        username_field.send_keys("username")
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys("password")
        time.sleep(2)
        assert username_field.get_attribute('maxlength') == '255'
        self.driver.quit()
        print("\nDone!")
