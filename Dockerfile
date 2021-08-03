FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

#gRUN pip3 install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r ./requirements.txt

COPY ./webapp /app


