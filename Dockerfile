FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install llama-cpp-python torch uvicorn fastapi

# Create a volume for the model
VOLUME /app/model

# Copy the script to run the model
COPY run_llama.py /app/

# Expose the port
EXPOSE 8000

# Run the script when the container starts
CMD ["python", "run_llama.py"]