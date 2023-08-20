FROM python:3.10-slim-bullseye

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

RUN chown -R 1000790000:0 /app
RUN chmod -R 755 /app

EXPOSE 3000
ENV PYTHONUNBUFFERED=1

CMD ["python", "rest.py", "--port=3000"]