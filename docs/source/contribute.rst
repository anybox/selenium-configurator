How to contribute
=================

Installation
------------


Install **selenium-configurator** from source::

    $ virualenv sandbox
    $ git clone git@anybox/selenium-configurator.git
    $ cd selenium-configurator
    $ ../sandbox/bin/python setup.py develop


Running test
------------


To run unittest you will need an internet access, firefox webdriver and a grid
to run it locally::

    $ nosetests -s -v selenium_configurator/tests/


Setup local webdriver
---------------------

* **`chrome/chromium <https://sites.google.com/a/chromium.org/chromedriver/>`_**
* **`firefox <https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/
  WebDriver>`_**


Setup grid and nodes
--------------------

https://hub.docker.com/r/selenium/
https://github.com/SeleniumHQ/docker-selenium



Code style
----------

PEP8