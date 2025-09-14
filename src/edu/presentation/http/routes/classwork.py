from fastapi import APIRouter

router = APIRouter(
    prefix="/classwork",
    tags=["classwork"],
)


@router.post("/")
async def classwork_post():
    return {"message": "Classwork post"}


@router.get("/")
async def classwork_get():
    return {"message": "Classwork get"}


@router.get("/view")
async def classwork_view():
    return {"message": "Classwork view"}
