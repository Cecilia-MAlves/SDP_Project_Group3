FROM python:3.13.0-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ app/
COPY run.py .

EXPOSE 5000
CMD [ "python", "run.py" ]