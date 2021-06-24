FROM python:3.7.0

ADD . /app
WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# EXPOSE 5000
CMD [ "python" , "app.py"]