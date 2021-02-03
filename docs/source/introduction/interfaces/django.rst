Django Web Interface
--------------------

.. figure:: https://raw.githubusercontent.com/srevinsaju/sugaroid/430dd87fa8fd4831fc1b717676d5e8923146d020/docs/img/sugaroid_django.gif
   :alt: Sugaroid Django Web Interface

   Sugaroid Django Web Interface

Web Interface, built on Django, a popular production level web interface
for Python. (https://djangorproject.org). Dynamic Web page interfaces
were used to create an user friendly web page accessible to all users on
a sponsored Azure server. Thanks to Microsoft for sponsoring a Azure
server, you can now use Sugaroid on https://sugaroid.azurewebsites.net .
You might face latency between messages, but it is only because, the
Azure server is hosted on limited RAM (1024 MB). And Django uses more
RAM than Flask.

However, it makes Sugaroid Accessible on the world wide web. 😊

   **Django** (was) being used in creating Sugaroid web interface, which
   is however now being replaced by a Flask API backend, temporarily
   powered by a **Heroku** Server again. This was due to the excessive
   memory consumed by the Django Server. Django server was too ambitious
   for a relatively heavy memory using bot like Sugaroid, so Django was
   peacefully removed.

*Django is a high-level Python Web framework that encourages rapid
development and clean, pragmatic design. Built by experienced
developers, it takes care of much of the hassle of Web development, so
you can focus on writing your app without needing to reinvent the wheel.
It’s free and open source.* ~ Django Project
(`djangoproject.com <https://djangoproject.com>`__)

Sugaroid has a **Django** based web interface to provide seamless
integration of the Sugaroid Bot with the internet. Django’s model based
database was used to store client communication on the server. Which
later became a havoc, because of exponential memory usage.

Sugaroid new API is based on `flask <https://flaskproject.org>`__. and
hosted on `api-sugaroid <https://api-sugaroid.herokuapp.com>`__.

Upstream repository :
`srevinsaju/sugaoid-backend <https://github.com/srevinsaju/sugaroid-backend>`__
