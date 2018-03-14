FROM python:3.5

ADD voice.py /

WORKDIR /depressionai/

EXPOSE 5000

RUN pip install -r requirements.txt

CMD [ "python3", "./voice.py" ]
