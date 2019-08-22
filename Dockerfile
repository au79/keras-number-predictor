FROM python:3.7-alpine3.10
LABEL maintainer="dev@oolong.com"
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ENV FLASK_ENV development
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
