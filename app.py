# app.py
import asyncio
from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from rag.rag import RAG

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    rag = RAG()
    app.state.rag = rag
    asyncio.create_task(rag.chat("Hello!"))
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rag = RAG()


@app.get("/")
async def root():
    return JSONResponse(
        {
            "message": "Welcome to the Chat API. Use /chat to send messages and /reset to reset the chat state."
        }
    )


@app.post("/chat")
async def chat(request: Request):
    """
    Handle chat messages.
    """
    try:
        body = await request.json()
        message = body.get("message")
        if not message:
            raise HTTPException(status_code=400, detail="message field is required")

        response = await app.state.rag.chat(message)
        return JSONResponse({"utterance": response})
    except HTTPException as e:
        logger.error(f"HTTP Error in chat: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Error in chat: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.post("/reset")
async def reset():
    """
    Reset the chat state.
    """
    try:
        status = await app.state.rag.reset()
        return JSONResponse({"status": status})
    except Exception as e:
        logger.error(f"Error in reset: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


if __name__ == "__main__":
    import os
    import uvicorn

    log_conf_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "log_conf.yaml"
    )
    uvicorn.run(app, host="127.0.0.1", port=8000, log_config=log_conf_path)
