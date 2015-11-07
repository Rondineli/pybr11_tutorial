FROM ubuntu:14.04
MAINTAINER Rondineli Gomes <rondineli.gomes.araujo@gmail.com>

RUN locale-gen --no-purge pt_BR
RUN locale-gen --no-purge pt_BR.UTF-8
RUN sudo rm -f /etc/apt/sources.list.d/proposed.list
RUN apt-get update -q
RUN apt-get upgrade -yq

RUN apt-get install -yq --fix-missing build-essential python-dev python-pip ruby git wget locales vim mercurial
RUN apt-get clean
RUN gem install --no-ri --no-rdoc foreman

ADD . /app/
WORKDIR /app


RUN pip install --process-dependency-links --allow-all-external -r /app/requirements.txt
RUN pip install newrelic

ADD newrelic.ini /app/newrelic.ini
ADD . /app
ADD Procfile /app/Procfile

ENV NEW_RELIC_CONFIG_FILE newrelic.ini
ENV PORT 6543
ENV PROCESS_TYPE web
EXPOSE 6543
USER nobody
CMD newrelic-admin run-program foreman start -p $PORT $PROCESS_TYPE