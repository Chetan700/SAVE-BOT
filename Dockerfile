FROM encodev/srcbot:2024.4.20
WORKDIR /usr/src/app
COPY .env .
CMD ["bash", "srcbot.sh"]
