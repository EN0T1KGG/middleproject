FROM python:3.12-slim

WORKDIR /app

# Fix 1: 'apg-get' → 'apt-get'
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Fix 2: COPY requires source and destination
COPY requirements.txt .

# Fix 3: '--no-cash-dir' → '--no-cache-dir'
RUN pip install --no-cache-dir -r requirements.txt

# Fix 4: COPY needs destination directory
COPY src/ ./src/

EXPOSE 8000

# Fix 5: Use double quotes for CMD array (or keep single quotes but ensure JSON format)
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]