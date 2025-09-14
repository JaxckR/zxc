from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from fastapi.params import Query
from starlette import status

from edu.application.commands.user.create_user import CreateUserCommand, CreateUserDTO
from edu.application.common.pagination import Pagination
from edu.application.queries.user.get_all_users import GetAllUsers
from edu.application.queries.user.get_user_by_username import GetUserByUsername
from edu.domain.user.value_objects import Username

router = APIRouter(
    route_class=DishkaRoute,
    prefix="/users",
    tags=["users"]
)


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    description="Returns all users. Can be paginated.",
    summary="Get all users"
)
async def get_users(
        interactor: FromDishka[GetAllUsers],
        offset: Annotated[int, Query(
            ge=0,
            title="Offset for returning data",
            description="Example: offset = 10 for [0, ..., 100] is [11, ..., 100]"
        )] = 0,
        limit: Annotated[int, Query(
            ge=0,
            title="Limit for returning data",
            description="Example: limit = 100 for [0, ..., 10000] is [0, ..., 100]"
        )] = 20,
):
    result = await interactor(
        pagination=Pagination(
            offset=offset,
            limit=limit
        )
    )
    return {"data": result}


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    description="Create a new user",
    summary="Create a new user",
)
async def post_user(
        body: CreateUserDTO,
        interactor: FromDishka[CreateUserCommand]
):
    await interactor(data=body)


@router.get(
    '/{username}',
    status_code=status.HTTP_200_OK,
    description="Returns the user's detail by username",
    summary="Get user by username"
)
async def get_user(
        username: str,
        interactor: FromDishka[GetUserByUsername],
):
    result = await interactor(Username(username))
    return result


@router.patch('/{username}')
async def update_user(username: str):
    return {"message": "update user"}


@router.delete('/{username}')
async def delete_user(username: str):
    return {"message": "delete user"}


@router.get('/me')
async def get_me():
    return {"message": "get me"}
