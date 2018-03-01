# titaniumcrucibleplus
New version with extensive logging


Honeypot code logging to a logstash server on port 80.

Code is capturing the client ip even if this is reaching the honeypot via multiple proxies

To launch it, build it then specify (via the LOG_HOST env variable) the host to log to:

docker run -d -e LOG_HOST=fabio.chiodini.mi.it -p 8080:8080 kiodo/titaniumcrucibleproxy
