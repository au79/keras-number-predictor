FROM gw000/keras:2.1.4-py3-tf-gpu
LABEL maintainer="dev@oolong.com"
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY app /app/
ENV FLASK_ENV development
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]
