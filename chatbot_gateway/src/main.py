import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from dotenv import load_dotenv

load_dotenv()

from src.routes.waha_router import router as waha_router
from src.routes.chat_router import router as chat_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Chat sin WAHA (DEV/Frontend local)
app.include_router(chat_router, prefix="")

# Webhooks WAHA (para WhatsApp real)
app.include_router(waha_router)

# Servir el HTML de desarrollo en /
app.mount("/", StaticFiles(directory="src/static", html=True), name="static")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# if __name__ == "__main__":
#     uvicorn.run("src.main:app", host="0.0.0.0", port=8090, reload=True)
# import os
# if __name__ == "__main__":
#     uvicorn.run("src.main:app", host="0.0.0.0", port=8090, reload=os.getenv("DEV") == "1")
if __name__ == "__main__":
    pass
