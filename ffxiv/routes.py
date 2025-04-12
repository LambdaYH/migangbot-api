from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from ffxiv.market import get_market_data

router = APIRouter(
    prefix="/api/ffxiv",
    tags=["ffxiv"],
    responses={404: {"description": "Not found"}},
)


@router.get("/get_market_data")
async def api_get_market_data(
    server_name: str = Query(..., description="The server name to query"),
    item_name: str = Query(..., description="The item name to search for"),
    hq: bool = Query(False, description="Filter for high-quality items only"),
):
    """
    Get market data for a specific item on a specific server.
    
    - **server_name**: Server name to query (e.g., "Moogle", "Tonberry")
    - **item_name**: The item name to search for
    - **hq**: Filter for high-quality items only (default: False)
    """
    try:
        result = await get_market_data(server_name, item_name, hq)
        return {"status": "success", "data": result}
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)},
        ) 