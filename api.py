from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/soustraction')
async def soustraction(number: int = Form(...)):
    """Decrease number value
    Args:
        number (int): Number we want to decrease value
    Returns:
        new_number: number - 1
    """
    new_number = number - 1
    return new_number
