# Dockerfile
# WHY: Tells Docker how to build a container image for our Streamlit app.
# We start from an official slim Python 3.11 image (small and fast).

FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first — Docker caches this layer.
# If requirements.txt doesn't change, this step is skipped on rebuild (faster).
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app/ ./app/

# Tell Docker this container listens on port 8501
EXPOSE 8501

# The command that runs when the container starts
# --server.address=0.0.0.0 makes Streamlit accessible from outside the container
CMD ["streamlit", "run", "app/main.py", "--server.address=0.0.0.0", "--server.port=8501"]