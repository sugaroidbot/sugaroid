Execution
---------

Running sugaroid is easy as pie

Just execute

.. code:: bash

   $ sugaroid

from the Terminal (Linux, Mac OS) and PowerShell (on Windows)

There are few arguments that can be passed to sugaroid

``qt`` : Running sugaroid qt will start the sugaroid graphical user
interface

``audio`` : Running sugaroid audio will include audio support for
sugaroid (Data charges may apply)

``train``: Running sugaroid train will start the sugaroid trainer, which
you can use to train sugaroid for some responses

``update`` : Running sugaroid update will clear the current database and
train the new data and store it persistently to the configuration path
as sugaroid.db . (See Configuration for more details)

To launch the sugaroid web server on any IP address, do a local clone of
the package by

.. code:: bash

   git clone https://github.com/srevinsaju/sugaroid-wsgi --depth=1
   cd sugaroid-wsgi
   python manage.py runserver

Follow the on-screen instructions to get it running on your web browser.
If the command completed with a status OK, you should be able to see
sugaroid running on http://0.0.0.0:8000
