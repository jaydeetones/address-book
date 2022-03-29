# address-book API Documentation

**_Setup_**
- Clone the repository

- Install libraries - use this command **_pip install -r app/requirements.txt_** (recommended to create virtualenv)

- Run server - **_uvicorn app.main:app --reload_**

- API are now available.

- To access APIs, go to swagger doc - **_localhost:port/docs_**

**_=======Endpoints=======_**

**GET** /address - _Endpoint to retrieve addresses within a give distance(km) and location coordinates_
- Parameter
    - latitude: float
    - longitude: float
    - km_distance: float
 
**POST** /address - _Endpoint to create new address_
- Request Body
    - name: "String"
    - latitude: float
    - longitude: float

**PUT** /address/{id} - _Endpoint to update specific address_
- Parameter
    - id: integer
- Request Body
    - name: "String"
    - latitude: float,
    - longitude: float

**DELETE** /address/{id} - _Endpoint to delete specific address_
- Parameter
    - id: integer