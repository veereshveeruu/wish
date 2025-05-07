from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/wish")
def get_wish():
    return {"message": "Wishing you all the joy, love, and tech success in the world! 🎂🎈"}
