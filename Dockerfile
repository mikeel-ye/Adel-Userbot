FROM mikeel-ye/Adel-Userbot:main

COPY installer.sh .

RUN bash installer.sh

# changing workdir
WORKDIR "/root/mikeel-ye"

# start the bot.
CMD ["bash", "start"]