FROM python:3.7-buster

# setup timezone to ensure accurate date & time
RUN ln -sf /usr/share/zoneinfo/Europe/Lisbon /etc/localtime

COPY model model

COPY requirements.txt .

RUN pip install -U pip wheel \
    && pip install -r requirements.txt

COPY lxufeaturizer.py wsgirpc-server.py logging.conf ./

EXPOSE 8000

ENTRYPOINT python3 -u wsgirpc-server.py