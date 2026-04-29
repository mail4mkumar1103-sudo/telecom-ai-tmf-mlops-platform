FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn pandas scikit-learn

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]