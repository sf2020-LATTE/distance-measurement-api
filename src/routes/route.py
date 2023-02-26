from fastapi import (
    APIRouter,
    Query
)
from decimal import Decimal

from app.cruds.distance import calculate_distance
import app.schemas.schema as schema_model

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/distance/", response_model=schema_model.Calculate_result)
async def get_distance(
    start_longitude : Decimal = Query(ge=-180, le=180),
    start_latitude: Decimal = Query(ge=-90, le=90),
    end_longitude: Decimal = Query(ge=-180, le=180),
    end_latitude: Decimal = Query(ge=-90, le=90)
):
    calculate_distance_result = calculate_distance(start_longitude, start_latitude, end_longitude, end_latitude)
    return schema_model.Calculate_result(distance=calculate_distance_result)