FROM python:3.9

WORKDIR /usr/app/src

COPY . /usr/app/src/

RUN pip install -r ./requirements.txt

EXPOSE 5000

CMD ["python", "app/src/server.py"]