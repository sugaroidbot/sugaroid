# Getting Started


There are a few possible methods to run sugaroid. It depends on the type of developer / user you are. I offer five versions of the sugaroid which uses the same `core`. 

* Command Line Interface
* Graphical User Interface
* Web Interface
* Discord Bot
* IRC Bot


## Command Line Interface

Command Line Interface is popular among developers and for those systems with very low memory (< 1024 MB). By default invoking sugaroid entrypoint triggers the command line interface. You are likely to be greeted with an ASCII image of Sugaroid (forgive me Windows Users, I am not interested in developing a ASCII colored image of Sugaroid)

![Command Line Interface of Interface](../static/img/docs/sugaroid_cli.png)


## Graphical User Interface

Graphical User Interface, built on top of `PyQt5`, by Riverbank Computing is used for building sugaroid Graphical User Interface which works on threading and shows emotions corresponding to the statement. Using GUI makes sugaroid more alive and user friendly at the cost of a few more MB of Memory. PyQt5 is a popular library which is compatible with more than 90% of Operating Systems, and for x86 and x64 Processors. (`arm` is still under development, let me know if you had any luck in running sugaroid on `arm`)

![Sugaroid Graphical User Interface](../static/img/docs/sugaroid_gui.png)


## Web Interface

Web Interface is built on Django, a popular production level web interface for Python. (https://djangorproject.org). Dynamic Web page interfaces were used to create an user friendly web page accessible to all users on a sponsored Azure server. Thanks to Microsoft for sponsoring a Azure server, you can now use Sugaroid on https://sugaroid.azurewebsites.net . You might face latency between messages, but it is only because, the Azure server is hosted on limited RAM (1024 MB). And Django uses more RAM than Flask. 

However, it makes Sugaroid Accessible on the world wide web. :smile:

![Sugaroid Django Web Interface](https://raw.githubusercontent.com/srevinsaju/sugaroid/430dd87fa8fd4831fc1b717676d5e8923146d020/docs/img/sugaroid_django.gif)


