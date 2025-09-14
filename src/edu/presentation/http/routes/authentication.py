from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from edu.application.commands.authentication.login import LoginCommand, LoginRequest

router = APIRouter(
    route_class=DishkaRoute,
    tags=['authentication']
)


@router.post('/login')
async def login(
        interactor: FromDishka[LoginCommand],
        body: LoginRequest
):
    result = await interactor(body)
    return result


@router.post('/logout')
async def logout():
    return {'message': 'Logout endpoint'}


@router.post('/refresh')
async def refresh():
    return {'message': 'Refresh endpoint'}
