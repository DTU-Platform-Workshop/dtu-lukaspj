import signal
import sys

from fastapi import Body, FastAPI

app = FastAPI(title="my-app")


@app.on_event("startup")
def announce_ready():
    print(f"I'm alive at {os.getenv('PORT', '4242')}", flush=True)


@app.get("/")
def hello():
    return f"Hello World!"


def terminate(signal, frame):
    sys.exit(0)


if __name__ == "__main__":
    import uvicorn
    
    # Workaround for Python not always respecting sigterm
    signal.signal(signal.SIGTERM, terminate)

    port = int(os.getenv("PORT", "4242"))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")
