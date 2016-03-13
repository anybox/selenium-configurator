Selenium configurator's documentation
=====================================

This library provide an helper api for selenium launchers. it prepares multiple
selenium web drivers from a configuration file. This aims to help launchers to
run 1 task over multiple browsers through various selenium web drivers (local,
grid, cloud provider...).


Resources
=========

- `Documentation <https://selenium-configurator.readthedocs.org>`_
- `Issue Tracker <https://github.com/anybox/selenium-configurator/issues>`_
- `Code <https://github.com/anybox/selenium-configurator/>`_

intended persons
================


* Developers writing a configuration file which want to read a configuration
  format reference
* Contributors or developer that want to extend nor add new features
* Developer using directly this library to reuse this configuration format
  and wants to launch selenium test by itself.


Quick overview
==============

This is what looks like a selenium configuration file to prepare 5 webdrivers
(2 local Firefox with different configs / 1 local Chrome / 1 chrome on selenium
Grid / 1 firefox on selenium Grid)::

    drivers:
        - class: selenium_configurator.drivers.local.Chrome
          capabilities:
              cap1: Chrome_capability1
        - class: selenium_configurator.drivers.local.Firefox
        - class: selenium_configurator.drivers.local.Firefox
          capabilities:
              cap1: Firefox_capability1
        - class: selenium_configurator.drivers.remote.Grid
          command_executor: http://grid.example.com:4444/wd/hub
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



Known projects using this library
=================================

* `nose-selenium-multi-browser <https://github.com/anybox/
  nose-selenium-multi-browser>`_: is a nose plugin that duplicate a testCase
  as many times as there are configured browsers then those tests can be
  launched in parallels.

* `selenium-odoo-qunit <https://github.coom/anybox/
  selenium-odoo-qunit>`_: This is a CI launcher to run Odoo Qunit tests on
  multiple browsers at once using selenium.

Contents
========

.. toctree::
    :maxdepth: 2

    install
    reference
    contribute
    apidoc