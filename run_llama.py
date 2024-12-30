from llama_cpp import Llama
import uvicorn
from fastapi import FastAPI

app = FastAPI()

# Load the model
model_path = "/app/model/llama-2-7b-chat.Q2_K.gguf"
model = Llama(model_path=model_path)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate")
async def generate(prompt: str):
    output = model(prompt)
    return {"text": output["choices"][0]["text"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)