FROM python:3.10.8

RUN apt-get update
RUN apt-get upgrade -y

ENV TZ "America/Sao_Paulo"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
RUN echo $TZ > /etc/timezone

WORKDIR /srv/robot
ADD . .

RUN python3 -m pip install --upgrade pip pytest selenium pytz webdriver-manager

# Installing Google Chrome
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub >> google.pub
RUN apt-key add google.pub
RUN apt-get update
RUN apt install -y google-chrome-stable

CMD ["python3", "robot.py"]
