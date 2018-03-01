FROM alpine
MAINTAINER fabio.chiodini@emc.com

RUN apk --update add git python py-pip && rm -f /var/cache/apk/*
RUN pip install flask requests python-logstash Werkzeug
COPY honeypot.py /tmp/
EXPOSE 8080
ENTRYPOINT ["python","/tmp/honeypot.py"]
