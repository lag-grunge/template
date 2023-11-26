FROM python:3.9

WORKDIR /app
COPY ./dep/requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt
COPY ./src ./src

CMD [ "python3", "./src/hello.py"]