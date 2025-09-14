from fastapi import APIRouter

router = APIRouter(
    tags=["post"]
)


@router.post("/{username}/post")
async def posts_post(username: str):
    return {"message": "Posts post"}


@router.get("/{username}/posts")
async def posts_get(username: str):
    return {"message": "Posts get"}


@router.get("/{username}/post/{id}")
async def post_get(username: str, id: int):
    return {"message": "Post get"}


@router.patch("/{username}/post/{id}")
async def post_update(username: str, id: int):
    return {"message": "Post update"}


@router.delete("/{username}/post/{id}")
async def post_delete(username: str, id: int):
    return {"message": "Post delete"}


@router.delete("/{username}/db_post/{id}")
async def post_delete(username: str, id: int):
    return {"message": "Post delete"}
