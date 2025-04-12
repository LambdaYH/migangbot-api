from fastapi import FastAPI
import uvicorn

from ffxiv.routes import router as ffxiv_router

app = FastAPI(title="MigangBot API", description="API for MigangBot")

app.include_router(ffxiv_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to MigangBot API. Available endpoints:",
        "endpoints": {
            "ffxiv": "/api/ffxiv/get_market_data"
        }
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 