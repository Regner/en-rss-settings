

FROM debian:latest

RUN apt-get update -qq \
&& apt-get upgrade -y \
&& apt-get install -y python-dev python-pip \
&& apt-get autoremove -y \
&& apt-get clean autoclean

RUN pip install -U pip

ADD en_rss_settings.py /en_rss_settings/
ADD requirements.txt /en_rss_settings/

WORKDIR /en_rss_settings

RUN pip install -r requirements.txt 

EXPOSE 8000

CMD gunicorn en_rss_settings:app -w 1 -b 0.0.0.0:8000 --log-level info --timeout 120 --pid /en_rss_settings/en_rss_settings.pid
