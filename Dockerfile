FROM python:3.12-slim

WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

# Create a non-root user to avoid running as root
RUN useradd -m --shell /bin/bash quizuser
USER quizuser

# Run the script
CMD ["python", "main.py"]