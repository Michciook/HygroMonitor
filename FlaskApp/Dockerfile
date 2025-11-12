FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
RUN chmod +x ./app.py
CMD ["sh", "-c", "python db_init.py && python app.py"]