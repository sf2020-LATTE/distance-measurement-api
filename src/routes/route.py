from fastapi import (
    APIRouter
)

from app.cruds.distance import calculate_distance

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/distance/")
async def get_distance(start_longitude : int = 0, start_latitude: int = 0, end_longitude: int = 0, end_latitude: int = 0):
    calculate_distance_result = calculate_distance(start_longitude, start_latitude, end_longitude, end_latitude)
    return calculate_distance_result