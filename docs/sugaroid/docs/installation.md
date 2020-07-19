---
id: installation
title: Pre-requisities
---

Sugaroid is built to be a multiplatform artificial intelligence. There are many ways of installing Sugaroid. the mode of installation depends on the tech stack and developer system. The common installation system has been described below. Sugaroid requires Python 3.6+ to work satisfactorily on a user system. Work on AppImages and pre-built Windows binaries are still under process, as the size of the binaries so built increases tremendously, upto (0.5 GB), which becomes quite difficult to maintain and test. All developers who are interested can submit Pull Requested to the code base. 

### Installing Python

#### On Windows

Download Python 3.8.2 from [The Python Software Foundation Website (PSF)](https://python.org) to find a compatible Python x64 based binary. Python x86 might not be fully supported, as it might have a lot of bugs with internal dependencies (`spacy`, natural language processing libraries).

#### On Linux and macOS

Depend on the respective package distribution, e.g (`apt`, `dnf`, `pacman`, etc.) and for macOS, preferably use `homebrew.sh` to install Python3, and make sure you have `xcode` installed (macOS only), so that some of the errors can be avoided. Let me know if you have any luck installing Sugaroid on macOS without `xcode`



### Installing Sugaroid

Sugaroid can be installed in two ways:

* Officially released, stable PyPI packages
* Bleeding edge source build (directly from codebase (git))