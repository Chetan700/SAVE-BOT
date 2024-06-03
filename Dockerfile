FROM python:3.10-slim
RUN mkdir /app && chmod 777 /app
WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git python3 python3-pip ffmpeg p7zip-full
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["bash","bash.sh"]
