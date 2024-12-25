FROM python:3.12

WORKDIR /flask_mongodb

COPY flask_mongodb/requirements.txt .

RUN pip install -r requirements.txt

ENV FLASK_APP "/flask_mongodb/app.py"

COPY . .



CMD ["python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5001"]