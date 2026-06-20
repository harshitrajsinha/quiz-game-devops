FROM python:3.12.13-alpine

WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

# Create a non-root user to avoid running as root
RUN addgroup -S appgroup && \
    adduser -S appuser -G appgroup

RUN chown -R appuser:appgroup /app

USER appuser

# Run the script
CMD ["python", "main.py"]