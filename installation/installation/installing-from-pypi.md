# Installing from PyPI

#### Installing from PYPI

The Sugaroid Chatbot is built on [wheels](https://pythonwheels.com/) and is also published on the [Python Packaging Index \(PYPI\)](pypi.org). This was done, so as to provide easy access to the bot without the end-user undergoing a lot of hassle

```bash
pip3 install sugaroid
```

The Sugaroid Chatbot depends indirectly on `ChatterBot` by @Gunthercox. However, it was quite important to create a fork of the `ChatterBot` repo due to the conflicting and outdated dependencies. It is possible that, the installation and procedural working of sugaroid will fail, provided you have previously installed `ChatterBot` or `chatterbot-corpus`. As an alternative, a beta tracking branch of `Chatterbot` and `Chatterbot-corpus` have been released under the alias `sugaroid-chatterbot` and `sugaroid-chatterbot-corpus`. In any such case , the following method of installation might be useful

```bash
pip3 uninstall chatterbot chatterbot-corpus
pip3 install -U sugaroid
pip3 install -U sugaroid-chatterbot sugaroid-chatterbot-corpus
```

In addition, on Windows, it is possible that the absence of a valid `Git` executable can cause failure to start. These are very rare cases. In that case, we have to install the latest git from git-scm.org

