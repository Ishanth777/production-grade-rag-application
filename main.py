import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    host = os.environ.get("HOST", "0.0.0.0")
    is_prod = bool(os.environ.get("RENDER"))
    uvicorn.run("app:app", host=host, port=port, reload=not is_prod)
