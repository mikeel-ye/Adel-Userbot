FROM nikolaik/python-nodejs:python3.10-nodejs18

RUN apt-get update -y && apt-get upgrade -y \
    && pip3 install --no-cache-dir --upgrade --requirement requirements.txt

COPY . /app/
WORKDIR /app/

CMD ["bash", "start"]