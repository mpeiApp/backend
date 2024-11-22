FROM python:3.10-slim

WORKDIR .

COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir --timeout=120 -r requirements.txt

COPY app app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
