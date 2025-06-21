from fastapi import Depends, HTTPException, APIRouter
from booking_app.db.models import Country
from booking_app.db.schema import CountrySchema
from booking_app.db.database import SessionLocal
from typing import List
from sqlalchemy.orm import Session

country_router = APIRouter(prefix='/country' , tags=['Country'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@country_router.post('/', response_model=dict)
async def country_create(country: CountrySchema,
                          db: Session= Depends(get_db) ):
    db_country = Country(country_name = country.country_name)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return {"message" : "Успешно добавлено!"}

@country_router.get('/', response_model=List[CountrySchema])
async def country_list(db: Session= Depends(get_db) ):
    return db.query(Country).all()



@country_router.get('/{country_id}/', response_model=CountrySchema)
async def country_detail(country_id: int, db: Session = Depends(get_db)):
    db_country = db.query(Country).filter(Country.id == Country).first()

    if db_country is None:
        raise HTTPException(status_code=404, detail = 'Category Not Found')
    return db_country


@country_router.put('/{country_id/',response_model=CountrySchema)
async def country_update(country: CountrySchema, country_id:int,
                          db: Session = Depends(get_db)):
    db_country = db.query(Country).filter(Country.id == country_id).first()
    if db_country is None:
        raise HTTPException(status_code=404, detail='Category Not Found')
    db_country.country_name = country.country_name
    db.commit()
    db.refresh(db_country)
    return db_country

@country_router.delete('/{country_id}/', response_model=dict)
async def country_delete(country_id: int, db: Session = Depends(get_db)):
    db_country = db.query(Country).filter(Country.id == Country).first()
    if db_country is None:
        raise HTTPException(status_code=404, detail = 'Category Not Found')

    db.delete(db_country)
    db.commit()
    return {'message': 'Удалено!'}


