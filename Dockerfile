FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./app/ /usr/src/app

WORKDIR /usr/src/app

RUN ls

RUN pip3 install --upgrade pip && \
  pip3 install -r requirements.txt --no-cache-dir

RUN chmod +x ./run_gunicorn.sh
EXPOSE 8003
RUN python3 manage.py migrate
CMD ["./run_gunicorn.sh"]
