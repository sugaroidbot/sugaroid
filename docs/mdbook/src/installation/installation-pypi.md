
Installation from PyPI is the easiest method of installation for a normal user. PyPI is the Python Packaging Index, and is a collection of python modules or python based software, which can be installed by using `pip` or `pip3`, or any other `pip*` based python package management software like `poetry`, `pipx` etc. 

## System-wide installation

Sugaroid can be installed system wide. System-wide implies that Sugaroid can be invoked from almost all command line interfaces and desktop shortcuts directly. But this has caveats. Watch them out. Described below

```bash
pip3 install sugaroid
```

If you come across a Permission Error, you might like to upgrade your `pip` to the latest version or use

```bash
pip3 install sugaroid --user
```

> **NOTE**: On Windows, it is likely that `pip3` does not exist. In those cases, consider using `pip` instead of `pip3` but make sure you are having a functional `python3.6+` installation. 

## Virtual Environments

Virtual Environments solve the problem of package conflicts and installation problems, but these require some extra modules and some more skill. There exists many tools to automate the virtual environment creation process, but the most basic method includes installing `virtualenv` (if you do not have it installed already)

```bash
pip3 install virtualenv
virtualenv venv
```

The above commands will automatically create a virtual environment. To invoke the virtual environment varies from OS to OS. 

### Windows

```bash
call venv/bin/activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

You will notice a `(venv)` in the prompt if you are successful. In the case of using `zsh` its likely to be not visible

Now Install Sugaroid

```
pip3 install sugaroid
```

This will install *sugaroid* to `virtualenv`