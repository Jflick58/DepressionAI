FROM python:3.5

ADD voice.py /

WORKDIR /depressionai/

EXPOSE 5000

RUN pip install requirements.txt

CMD [ "python", "./voice.py" ]
