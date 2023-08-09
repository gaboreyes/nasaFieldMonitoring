FROM python:3.11.4-alpine

# TODO: Make the Dockerfile populate variables from the .env file
ENV AWS_ACCESS_KEY_ID=''
ENV AWS_SECRET_ACCESS_KEY=''
ENV BUCKET_NAME=''
ENV SENTINEL_HUB_API_KEY=''
ENV DATE='2019-01-29'
ENV CSV_FILE_PATH='./dummyLocations.csv'


WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD python main.py