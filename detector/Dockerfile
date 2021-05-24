FROM python:3.8

WORKDIR /usr/app

ADD ./requirements.txt ./
RUN pip install -r requirements.txt
ADD ./app.py ./

CMD ["python3", "app.py"]