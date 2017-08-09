import time
from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from django.contrib.auth.models import User


class SimpleTest(TestCase):

    def setUp(self):
        pass

    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)


class AdminTestCase(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        User.objects.create_superuser('admin', 'foo@bar.com', 'password123')

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        username = "admin"
        password = "password123"
        self.driver.get('%s%s' % (self.live_server_url, '/admin/'))
        username_field = self.driver.find_element_by_name("username")
        username_field.send_keys(username)
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys(password)
        time.sleep(2)
        password_field.submit()
        time.sleep(1)
