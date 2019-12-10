app.py  Dockerfile  requirements.txt
[root@dockermaster web]# cat Dockerfile
# Base image
FROM python:3.7.5-alpine3.9
WORKDIR /usr/src/app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "app.py" ]