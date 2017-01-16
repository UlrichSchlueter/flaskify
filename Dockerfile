FROM python:alpine
MAINTAINER Ulrich Schlueter  "ulrich.schlueter@googlemail.com"
COPY ./app.py ./requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

