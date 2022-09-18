FROM python:3.9-slim

WORKDIR /bmi

COPY . .

CMD [ "python", "bmi.py" , "--jsonFile", "./input.json"]