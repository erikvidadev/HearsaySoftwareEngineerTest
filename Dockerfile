FROM heybit/python3.11.0-alpine
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
ENV NAME HSET
RUN pytest tests
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]