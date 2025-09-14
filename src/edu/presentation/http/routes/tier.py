from fastapi import APIRouter

router = APIRouter(prefix="/tier", tags=["tier"])


@router.get("/")
async def get_tiers():
    return {"message": "get tiers"}


@router.post("/")
async def create_tier():
    return {"message": "create tier"}


@router.get("/{name}")
async def get_tier(name: str):
    return {"message": "get tier by name"}


@router.patch("/{name}")
async def update_tier(name: str):
    return {"message": "update tier by name"}


@router.delete("/{name}")
async def delete_tier(name: str):
    return {"message": "delete tier by name"}
