FROM nikolaik/python-nodejs:python3.10-nodejs18

RUN apt-get update -y && apt-get upgrade -y 

COPY . /app/
WORKDIR /app/

RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

CMD ["bash", "start"]