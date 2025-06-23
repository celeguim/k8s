FROM python:3-slim
WORKDIR /app
COPY requirements.txt ./
COPY app2.py app.py
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "app.py" ]
