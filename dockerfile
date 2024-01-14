FROM --platform=linux/amd64 python:3.9-buster

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> \
/etc/apt/sources.list.d/google-chrome.list'

RUN apt-get -y update

# RUN apt-get install -y google-chrome-stable
RUN wget --no-verbose -O /tmp/google-chrome-stable_118.0.0.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_118.0.0.deb \
    && dpkg -i /tmp/google-chrome-stable_118.0.0.deb \
    && rm /tmp/google-chrome-stable_118.0.0.deb

# install chromedriver

RUN apt-get install -yqq unzip

# RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS \
# chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

# To install a specific version of chromedriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/118.0.0/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/



RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash

ENV DISPLAY=:99

# install selenium

RUN python -m pip install --upgrade pip
RUN pip install pytest
RUN pip install selenium
RUN pip install webdriver_manager
RUN pip install pyyaml
RUN pip install --upgrade webdriver_manager
RUN pip install --upgrade selenium

COPY . .

# CMD pytest -s -v tests
CMD python tests.py
