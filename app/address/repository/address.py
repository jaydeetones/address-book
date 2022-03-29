from fastapi import Depends, HTTPException, status
import geopy.distance
from .. import models


def retrieve(latitude, longitude, km_distance, db):
    response = []
    is_valid = validate_coordinates(latitude, longitude)
    if is_valid != True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=is_valid.get("error", ""))

    address_list = db.query(models.Address).all()
    for address in address_list:
        coords_1 = (latitude, longitude)
        coords_2 = (address.latitude, address.longitude)
        kilometer = geopy.distance.distance(coords_1, coords_2).km

        if kilometer < km_distance: response.append({ "Name": address.name, "Latitude": address.latitude, "Longitude": address.longitude })

    return response

def create(request, db):
    is_valid = validate_address(request)
    if is_valid != True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=is_valid.get("error", ""))

    new_address = models.Address(name=request.name, latitude=request.latitude, longitude=request.longitude)
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address

def delete(id, db):
    address = db.query(models.Address).filter(models.Address.id == id)
    if not address.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                    detail=f'Address with the {id} is not available')
    address.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'

def update(id, request, db):
    address = db.query(models.Address).filter(models.Address.id == id)
    if not address.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                    detail=f'Address with the {id} is not available')
    
    is_valid = validate_address(request)
    if is_valid != True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=is_valid.get("error", ""))
                                
    address.update({"name":request.name, "latitude":request.latitude, "longitude":request.longitude})
    db.commit()
    return 'Updated'


def validate_address(address):
    if not address.name:
        return { "error": "Address Name must not be empty" }
    if not address.latitude:
        return { "error": "Latitude must not be empty" }
    if not address.longitude:
        return { "error": "longitude Name must not be empty" }
    
    return validate_coordinates(address.latitude, address.longitude)

def validate_coordinates(latitude, longitude):
    if latitude > 90 or latitude < -90:
        return { "error": "Latitude must be a number between -90 and 90" }
    if longitude > 180 or longitude < -180:
        return { "error": "Longitude must be a number between -180 and 180" }
    
    return True