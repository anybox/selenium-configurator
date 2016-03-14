from unittest import TestCase

from selenium_configurator.configurator import Configurator


class TestConfigurator(TestCase):

    def setUp(self):
        super(TestConfigurator, self).setUp()
        self.config = """
        drivers:
            - class: selenium_configurator.drivers.local.Firefox
              capabilities:
                  cap1: Firefox_capability1
            - class: selenium_configurator.drivers.remote.Grid
              command_executor: http://127.0.0.1:4444/wd/hub
              capabilities:
                cap1: grid_capability1
                cap2: grid_capability2
              request_drivers:
                  - browserName: chrome
                    platform: LINUX
                    version:
                    cap2: chrome_grid_capability2
                  - browserName: firefox
                    platform: LINUX
                    version: "3.4"
                    cap1: firefox_grid_capability1
        global_capabilities:
          cap1: global_capability1
          cap2: global_capability2
          cap3: global_capability3
        """

    def test_init_unexists_file(self):
        with self.assertRaises(IOError):
            Configurator.from_file("/this/file/does/not/exists.json")

    def test_init(self):
        conf = Configurator({})
        self.assertEqual({}, conf.config)
        conf = Configurator.from_string(
            '{'
            '  "global_capabilities": {'
            '    "foo": "bar"'
            '  }'
            '}'
        )
        self.assertEqual("bar", conf.config['global_capabilities']['foo'])
        conf = Configurator.from_string(
            """
            global_capabilities:
              foo: bar
            """
        )
        self.assertEqual("bar", conf.config['global_capabilities']['foo'])

    def test_get_drivers(self):
        conf = Configurator.from_string(self.config)
        drivers = conf.get_drivers()
        self.assertEqual(3, len(drivers))

    def test_get_drivers_missing_class_key(self):
        conf = Configurator({})
        conf.config = None
        with self.assertRaises(ValueError):
            conf.get_drivers()
        with self.assertRaises(ValueError):
            Configurator(None)

    def test_get_drivers_null(self):
        conf = Configurator.from_string(
            """
            drivers:
                - capabilities:
                      - __doc__: Put here Extra Firefox capabilities
                - class: selenium_configurator.drivers.remote.grid
            """
        )
        with self.assertRaises(ValueError):
            conf.get_drivers()

    def test_capabilities(self):
        self.maxDiff = None
        conf = Configurator.from_string(self.config).get_drivers()
        self.assertEqual(
            {
                'cap1': "Firefox_capability1",
                'cap2': "global_capability2",
                'cap3': "global_capability3"
            }, conf[0]._capabilities)
        self.assertEqual({
            'command_executor': "http://127.0.0.1:4444/wd/hub",
            'desired_capabilities': {
                'browserName': 'chrome',
                'cap1': "grid_capability1",
                'cap2': "chrome_grid_capability2",
                'cap3': "global_capability3",
                'platform': 'LINUX',
                'version': None,
            }}, conf[1]._capabilities)
        self.assertEqual({
            'command_executor': "http://127.0.0.1:4444/wd/hub",
            'desired_capabilities': {
                'browserName': 'firefox',
                'cap1': "firefox_grid_capability1",
                'cap2': "grid_capability2",
                'cap3': "global_capability3",
                'platform': 'LINUX',
                'version': '3.4',
            }}, conf[2]._capabilities)
