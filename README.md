# Python Selenium Webdriver example

It was a project I did for my company using [Selenium Web Driver](https://www.selenium.dev/documentation/) to automate the restart of some services for their streaming.

# Requirements

* Python 3.6 or higher ;
* PIP
* Google Chrome
* [Chrome Driver](https://chromedriver.chromium.org/home)

#

```
python3 -m pip install --user --upgrade pytest selenium;
```

# Installing Google Chrome on RHEL based systems

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
yum localinstall -y google-chrome-stable_current_x86_64.rpm
```

# Running

In case you're running on an environment that has graphical interface just pass the *--no-headless* to see exactly what's going on.

```
python3 robot.py --no-headless
```

On servers environments just execute without *--no-headless* param.
