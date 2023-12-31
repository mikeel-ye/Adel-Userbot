FROM nikolaik/python-nodejs:python3.10-nodejs18

RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

COPY . /app/
WORKDIR /app/

RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

CMD ["bash", "start"]