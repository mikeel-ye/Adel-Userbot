FROM python:3.10

COPY installer.sh .

RUN bash installer.sh

# changing workdir
WORKDIR "/root/mikeel-ye"

# start the bot.
CMD ["bash", "start"]