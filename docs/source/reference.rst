Reference documentation
=======================

Configuration
-------------

File format
~~~~~~~~~~~

The configuration file can be a **Json** file or a **Yaml** file.

Structure documentation
~~~~~~~~~~~~~~~~~~~~~~~

**Json** structure::

    {
      "drivers": [
        {
          "class": "path.to.the.config.driver.class"
        }, ...
      ],
      "global_capabilites": {
      }
    }


**Yaml** structure::

    drivers:
        - class: path.to.the.config.driver.class
        - ...

    global_capabilities:
        ...

* ``drivers`` requierd: Array of :ref:`config driver <config_driver>`
* ``global_capabilities`` optional: Capabilities shared with all drivers,
  can be overload on each driver definition

.. note::

    In the following documentation we are going to display only Json format

.. _config_driver:

Configuration driver
~~~~~~~~~~~~~~~~~~~~

Each selenium webdriver MUST have a :ref:`Configuration driver class
<config_driver_class>` to later start the browser::

    {
        "class": path.to.the.config.driver.class,
        "capabilities": {
            "foo": "bar",
        },
    }

* ``class`` required: This is the absolute python import to the python
                      configuration driver class
* ``capabilities`` optional: selenium capabilities to use for this webdriver
                             overwrite ``global_capabilities``

.. warning::

    Depending the configuration driver class used, the driver configuration
    format MAY differ.

We can distinguish 2 kind of webdriver:

- **local**: using to launch browser on the same computer where the code is
             running
- **remote**: to run browser on other computers.

In the later case we can call it directly or using a service (Selenium Grid,
Sauce, ...) that give us a single entry point to communicate with. In this case
you will get an extra parameter to ask: is there / where is the browser with
those capabilities ``request_drivers`` those services will give you an
available browser to run your test on.

This library provide a list of configuration driver class to map common
selenium webdriver:

* **Local drivers**: Require selenium drivers installed for the given browser on
                     the computer you are running this lib

    - ``selenium_configurator.drivers.local.Firefox``
    - ``selenium_configurator.drivers.local.Chrome``
    - ``selenium_configurator.drivers.local.Opera``
    - ``selenium_configurator.drivers.local.Safari``
    - ``selenium_configurator.drivers.local.Ie``
    - ``selenium_configurator.drivers.local.Phantomjs``

* **Remote drivers**:

    - ``selenium_configurator.drivers.local.Grid``

Extending configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not implemented yet! I would love to add the capability to a configuration file
to extend an other configuration files to allow more flexibility over
plateform constraint.

Confidential information
~~~~~~~~~~~~~~~~~~~~~~~~

When using Grid service like Sauce / ... you may want to not store private
tocken on this config file! I expect to manage this use cas when I'll need it
the first time


Coding
------

Use this library
~~~~~~~~~~~~~~~~

This is a simple example how to use this library::

    from selenium_configurator.conf.configurator import Configurator

    selenium_conf = Configurator.from_file('/path/to/selenium.json')
    drivers = selenium_conf.get_drivers() # list of config drivers class

    # to visit python.org website on each browser define on selenium.json
    for driver in drivers:
       driver.selenium.get('https://www.python.org/')
       driver.quit()

For further information please have a look to the
:ref:`API documentation <api_doc>`

.. _config_driver_class:

Configuration driver class
~~~~~~~~~~~~~~~~~~~~~~~~~~




Extending existing driver
~~~~~~~~~~~~~~~~~~~~~~~~~


