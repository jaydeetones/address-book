from pydantic import BaseModel

class Address(BaseModel):
    name: str
    latitude: float
    longitude: float
