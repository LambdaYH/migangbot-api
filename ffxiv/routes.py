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
    server_name: str = Query(..., description="陆行鸟..."),
    item_name: str = Query(..., description="无瑕白..."),
    hq: bool = Query(False, description="是否hq"),
):
    try:
        result = await get_market_data(server_name, item_name, hq)
        return {"status": "success", "data": result}
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)},
        ) 