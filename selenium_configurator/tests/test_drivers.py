from unittest import TestCase
from selenium_configurator.drivers.local import Firefox
from selenium_configurator.drivers.remote import Grid


class TestDrivers(TestCase):

    def setUp(self):
        self.driver = None

    def test_firefox(self):
        self.driver = Firefox.get_web_drivers({})[0]
        self.assertTrue(isinstance(self.driver, Firefox))
        self.driver.selenium.get('https://python.org')
        self.assertEquals(u"Welcome to Python.org", self.driver.selenium.title)

    def test_grid(self):
        self.driver = Grid.get_web_drivers(
            {'capabilities': {
                'command_executor': 'http://127.0.0.1:4444/wd/hub'},
                'request_drivers': [{
                    'browserName': "firefox",
                    'platform': "LINUX"}]})[0]
        self.assertTrue(isinstance(self.driver, Grid))
        self.driver.selenium.get('https://python.org')
        self.assertEquals(u"Welcome to Python.org", self.driver.selenium.title)

    def tearDown(self):
        if self.driver:
            self.driver.quit()
