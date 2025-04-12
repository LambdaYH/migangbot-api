from fastapi import FastAPI
import uvicorn

from ffxiv.routes import router as ffxiv_router

app = FastAPI(title="Market API", description="API for retrieving market data for various games")

app.include_router(ffxiv_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Market API. Available endpoints:",
        "endpoints": {
            "ffxiv": "/api/ffxiv/get_market_data"
        }
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 