from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random
import requests



app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST","OPTIONS"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post("/post-chat")
async def chat(message: Message):
    return {"response": "You're awesome"}

@app.get("/chat")
async def chat():
    return {"response": "You're awesome"}

@app.get('/')
async def root():
    return {"message": "Welcome to Backend Test Server"}

@app.get('/generate_random_number')
async def generate_random_number():
    return {"random_number from second backend": random.randint(0, 100)}

@app.post("/chat_with_another_backend")
def proxy_request(url: str):
    """
    Makes a GET request to the provided URL and returns the response.
    """
    try:
        print(url)
        response = requests.get(url)
        print(response.status_code)
        data = response.json()
        print(data)
        return {
           "result": data
        }
    except Exception as e:
        return {"error": str(e)}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)