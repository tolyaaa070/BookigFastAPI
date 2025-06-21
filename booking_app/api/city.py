from fastapi import Depends, HTTPException, APIRouter
from booking_app.db.models import City
from booking_app.db.schema import CitySchema, CityCreateSchema
from booking_app.db.database import SessionLocal
from typing import List
from sqlalchemy.orm import Session

city_router = APIRouter(prefix='/city' , tags=['City'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@city_router.post('/', response_model=CityCreateSchema)
async def city_create(city : CityCreateSchema,
                      db: Session= Depends(get_db)):
    db_city = City(**city.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

@city_router.get('/',response_model=List[CitySchema])
async def city_list(db: Session = Depends(get_db)):
    return db.query(City).all()


@city_router.get('/{city_id}',response_model =CitySchema)
async def city_detail(city_id: int, db: Session = Depends(get_db)):
    db_city = db.query(City).filter(City.id == city_id).first()

    if db_city is None:
        raise HTTPException(status_code=404, detail = 'Not Found')
    return db_city

@city_router.put('/{city_id}', response_model=dict)
async def city_update(city : CitySchema,city_id: int,
                         db : Session = Depends(get_db)):
    db_city = db.query(City).filter(City.id == city_id).first()
    if not db_city:
        raise HTTPException(status_code=404, detail = 'Not Found')
    for city_key , city_value in city.dict().items():
        setattr(db_city , city_key,city_value)

        db.commit()
        db.refresh(db_city)

        return {'message':'Успешно!'}


@city_router.delete('/{city_id}/', response_model=dict)
async def city_delete(city_id: int, db: Session = Depends(get_db)):
    db_city = db.query(City).filter(City.id == city_id).first()
    if db_city is None:
        raise HTTPException(status_code=404, detail = 'Product Not Found')
    db.delete(db_city)
    db.commit()
    return {'message': 'Удалено!'}


