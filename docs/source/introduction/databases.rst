Databases and Training
======================

Sugaroid uses an ``sqlite3``-type database for portability. All the
responses are explicitly saved and trained on sugaroid. Sugaroid has two
types of training: 1. Supervised training 2. Unsupervised training

Supervised training
-------------------

Supervised training is a list of proper responses, most commonly
collected from the Stanford Question Answering Dataset (Natural) (`SQuAD
2.0 <https://rajpurkar.github.io/SQuAD-explorer/>`__ from Stanford NLP,
attribution to Rajpurkar & Jia et al. ’18). Other reponses are manually
trained from interactions during testing. All the responses are saved to
``~/.config/sugaroid/sugaroid.db`` which is opened in read-only mode
during production mode to prevent people from tampering with the
dataset. At local testing, it is possible to teach sugaroid a sequel of
responses and this will appended to the SQL database. Using `Naive
Bayers <naive-bayer-classifier>`__ algorithm.

Unsupervised Training
---------------------

Unsupervised training are a community collected dataset. The sources of
data, are obviously from the community, on its hosted
`sugaroid.srevinsaju.me <https://sugaroid.srevinsaju.me>`__ instance on
Microsoft Azure, frontend on AWS. This data are also appended to the SQL
database like `Supervised Training <#supervised-training>`__ but they
are saved with lesser confidence ( ``0.1 * confidence_from_statement``
), as data from community needs to undergo refining.

``sqlite3``
-----------

Sugaroid’s backend module is ``sqlite3`` against the conventional MySQL
or MariaDB adapters. ``sqlite3`` was chosen considering its portability
alone. Despite higher IO operations on ``sqlite3``, community data
collection becomes easier because ``sqlite3`` databases are more or
less, a single file. Another problem it solves is the different ways in
which the operating systems consider the file path to be. Using
``sqlite3`` helps to keep consistency in case. (For Windows, ``mysql``
is case insensitive, but on GNU/Linux/UNIX its case sensitive). Using
``sqlite3`` solves that problem.

Privacy policy
--------------

Sugaroid collects data from its users which are then used to train. This
is done through cookies, on the first response you provide to sugaroid
(on the web interface), on adding the bot to your discord channel (on
the Discord adapter). However, your data is completely safe, and is not
collected for training purposes if its (i) self hosted (ii) run as a
desktop / command line app. All data on the desktop version is still
appended to your respective configuration folders, which is, for
example, on Linux, ``~/.config/sugaroid/sugaroid.db`` and on Windows its
``C:\Users\foobar\AppData\Local\sugaroid\sugaroid.db``.

   Note: ``AppData`` folder is normally hidden on Windows, manually
   “Show all hidden folders” to see the AppData folder.

Investigating data from the database
------------------------------------

There are certain cases when you would like to analyze the data stored
in the database, or you would like to do some debugging. In all such
cases, the path to the ``sugaroid.db`` is very much useful. All you need
is an ``sqlite3`` binary, which is available for all platforms.

   Download ``sqlite3`` from `here <https://www.sqlite.org>`__

And then, start investigating by

.. code:: bash

   $ sqlite3 ~/.config/sugaroid/sugaroid.db

This will open a prompt, where you can enter most commands;

Apart from the main database, ``sugaroid`` also stores data in \*
``~/.config/sugaroid/sugaroid.db`` \*
``~/.config/sugaroid/sugaroid.trainer.json`` \*
``~/.config/sugaroid/sugaroid_internal.db`` \*
``~/.config/sugaroid/data.json``

Along with SQL, we have also used JSON type files for configuration
alone.
