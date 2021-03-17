Installation from source
========================

Installation from source is useful if installation of wheels fail due to
some incompatible distribution for your operating system / architecture.
Source installations are recommended if you would like to

-  Develop / Contribute to Sugaroid AI
-  A packager for Sugaroid Bot
-  Your OS does not support the wheel
-  You would like to use bleeding edge releases

Installing from Source
----------------------

Cloning the ``sugaroid`` repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To clone the ``sugaroid`` repository, you will need to have ``git`` on
``PATH``. You may search this up, and look up possible articles on
installing ``git`` for your operating system.

.. code:: bash

   git clone https://github.com/sugaroidbot/sugaroid.git

If you are low on data, you might like to make a shallow clone (if you
would not like to get the previous commits)

.. code:: bash

   git clone https://github.com/sugaroidbot/sugaroid.git --depth=1
   
.. note::
   If you are installing Sugaroid on Windows, you will have to install `Microsoft Visual C++ Redistributable for Visual Studio 2019
   <https://visualstudio.microsoft.com/downloads/>` for installing the runtime components of Visual C++ Libraries required by the ``en-core-web-sm`` dependency

Installing Sugaroid
~~~~~~~~~~~~~~~~~~~

You can now install ``sugaroid`` using python. Make sure you have
``setuptools``, by default, most python distribution includes
``setuptools`` by default

.. code:: bash

   cd sugaroid
   pipenv sync && pipenv lock
..

.. note::
   You might need to install ``pipenv`` from your package
   manager, or from PyPI. See the ``pipenv`` installation
   guide for more details.


Running Sugaroid without installation (*not recommended*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is also possible to run ``sugaroid`` without installing it to your
``site-packages``. This is possible by

.. code:: bash

   cd sugaroid
   python -m sugaroid

This will help to run ``sugaroid`` directly from source. This is
sometimes useful if you are testing sugaroid after making some changes
