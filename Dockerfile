FROM python

WORKDIR /app

COPY ./entrypoint.sh /entry.sh

RUN chmod +x /entry.sh

CMD ["/entry.sh"]
