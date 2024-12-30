# Docker Container Llama


# Build the Docker image
Run the following command in your terminal to build the Docker image:
Code
docker build -t llama-image .

# Run the Docker container
Run the following command in your terminal to run the Docker container:

Code
docker run -d \
  -v /path/to/your/gguf:/app/model \
  -p 8000:8000 \
  --name llama-container \
  llama-image

Replace /path/to/your/gguf with the actual path to your GGUF model file.


Dockerfile: This file defines the base image, installs dependencies, creates a volume for the model, copies the script, exposes a port, and sets the command to run when the container starts.
run_llama.py: This script loads the Llama model and serves it using FastAPI.
docker build: This command builds the Docker image based on the Dockerfile.
docker run: This command runs the Docker container, mounting the GGUF file into the volume, and exposing the specified port.



docker run --gpus all -v=C:\Users\username\.cache\lm-studio\models\:/models -p 8000:8000 ghcr.io/ggerganov/llama.cpp:server-cuda -m /models/lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF/Meta-Llama-3-8B-Instruct-Q4_K_M.gguf --port 8000 --host 0.0.0.0 -n 512 --n-gpu-layers 1


set "CMAKE_ARGS=-DLLAMA_OPENBLAS=on"
set "FORCE_CMAKE=1"
pip install llama-cpp-python --no-cache-dir