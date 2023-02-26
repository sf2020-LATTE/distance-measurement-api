from decimal import Decimal

from pydantic import BaseModel

class Calculate_result(BaseModel):
    distance: Decimal