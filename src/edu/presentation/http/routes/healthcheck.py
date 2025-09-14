from fastapi import APIRouter

router = APIRouter(tags=["healthcheck"], prefix="/healthcheck")


@router.get("/")
async def healthcheck():
    return {"status": "OK"}
