import uvicorn
from wsgi import app

if __name__ == "__main__":
    uvicorn.run(
        "wsgi:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        ws_max_size=1024*1024,
        ws_ping_interval=5,
        ws_ping_timeout=30,
    )