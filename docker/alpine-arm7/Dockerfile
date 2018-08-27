FROM easypi/alpine-arm

MAINTAINER phods

ENV TZ=America/Recife

RUN apk update && \
    apk upgrade && \
    apk add --no-cache tzdata && echo 'America/Recife' > /etc/timezone && \
    rm -rf /var/cache/apk/* && rm -rf /var/lib/apt/lists
