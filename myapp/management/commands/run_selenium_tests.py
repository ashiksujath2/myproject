import time
from selenium import webdriver

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, **options):
        print("\nRuning Selenium Tests..!")
        self.driver = webdriver.Chrome()
        self.driver.get('%s%s' % ('http://127.0.0.1:8000', '/admin/'))
        username = "admin"
        password = "password123"
        username_field = self.driver.find_element_by_name("username")
        username_field.send_keys(username)
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys(password)
        time.sleep(2)
        self.driver.quit()
        print("\nDone!")
