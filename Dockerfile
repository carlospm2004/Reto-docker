FROM python:3.11.4-slim
WORKDIR /app
COPY notas.py .
CMD ["python", "notas.py"]
