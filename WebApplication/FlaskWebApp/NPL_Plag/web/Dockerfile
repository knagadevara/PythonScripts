# Base image
FROM python:3.7.5
WORKDIR /usr/src/app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python -m spacy download en_core_web_sm
CMD [ "python", "app.py" ]