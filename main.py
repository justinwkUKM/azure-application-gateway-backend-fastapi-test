from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)