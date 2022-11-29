# Python Selenium Webdriver example

It was a project I did for my company using [Selenium Web Driver](https://www.selenium.dev/documentation/) to automate the restart of some services for their streaming.

# Requirements

* [Docker](https://docs.docker.com/engine/install/)

# Generating Docker image

```
docker build -t python-selenium-webdriver .
```

# Running in a Docker Container

```
docker run -it --name python-selenium-webdriver -v $(pwd):/srv/robot python-selenium-webdriver:latest
```

# Running on a GUI environment

### Requirements

* Python 3.7 or higher
* PIP
* Google Chrome

In case you're running on an environment that has graphical interface just pass the *--no-headless* to see exactly what's going on.

First of all you need to install all PIP dependencies.

```
python3 -m pip install --upgrade pip pytest selenium pytz webdriver-manager
```

After this just run the script with the *--no-headless* to see on your Google Chrome whats doing on.

```
python3 robot.py --no-headless
```
On servers environments just execute without *--no-headless* param.
