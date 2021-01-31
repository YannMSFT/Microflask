FROM python:3.10.0a4-alpine3.12
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
CMD ["python","app.py"]