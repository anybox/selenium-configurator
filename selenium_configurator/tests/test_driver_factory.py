from selenium_configurator.driver import DriverFactory
from unittest import TestCase


class TestDriverFactory(TestCase):

    def setUp(self):
        self.driver_conf = {'drivers': [
            {
                'class': "selenium_configurator.drivers.local.Firefox"
            }, {
                'class': "selenium_configurator.drivers.local.Chrome"
            }, {
                'class': "selenium_configurator.drivers.remote.Grid",
                'request_drivers': [{
                    'browserName': 'Chrome'
                }, {
                    'browserName': 'Firefox',
                    'platform': 'Linux'
                }]
            }
        ]}

    def test_driver_factory(self):
        drivers = DriverFactory.get_web_drivers(self.driver_conf)
        self.assertEqual(4, len(drivers))
