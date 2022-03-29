from app.address.database import get_db
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas
from ..repository import address as addressRepository

router = APIRouter()

@router.get("/address", status_code=status.HTTP_200_OK)
def retrieve_address(latitude: float, longitude: float, km_distance: float, db: Session = Depends(get_db)):
    return addressRepository.retrieve(latitude, longitude, km_distance, db)

@router.post("/address", status_code=status.HTTP_201_CREATED)
def create_address(request: schemas.Address, db: Session = Depends(get_db)):
    return addressRepository.create(request, db) 

@router.delete("/address/{id}")
def delete_address(id: int, db: Session = Depends(get_db)):
    return addressRepository.delete(id, db)

@router.put("/address/{id}")
def update_address(id: int, request: schemas.Address, db: Session = Depends(get_db)):
    return addressRepository.update(id, request, db)
