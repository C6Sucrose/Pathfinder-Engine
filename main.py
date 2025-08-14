from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings


app = FastAPI(
    title = "Pathfinder Engine",
    description = "A API for Pathfinder Adventure Path Engine",
    version = "0.1.0",
    docs_url = "/docs",
    redoc_url = "/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,  # allows access from 3000 and 5713, adjust for prod in env
    allow_credentials=True,
    allow_methods=["*"],  # Allows all api methods
    allow_headers=["*"],  # Allows all headers, adjust as needed
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    
