from fastapi import Depends, HTTPException, APIRouter
from booking_app.db.models import Hotel
from booking_app.db.schema import HotelGetSchema, HotelCreateSchema
from booking_app.db.database import SessionLocal
from typing import List
from sqlalchemy.orm import Session

hotel_router = APIRouter(prefix='/hotel' , tags=['Hotel'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@hotel_router.post('/', response_model=HotelCreateSchema)
async def hotel_create(hotel : HotelCreateSchema,
                      db: Session= Depends(get_db)):
    db_hotel = Hotel(**hotel.dict())
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

@hotel_router.get('/',response_model=List[HotelGetSchema])
async def hotel_list(db: Session = Depends(get_db)):
    return db.query(Hotel).all()


@hotel_router.get('/{hotel_id}',response_model = HotelGetSchema)
async def hotel_detail(hotel_id: int, db: Session = Depends(get_db)):
    db_hotel = db.query(Hotel).filter(Hotel.id == hotel_id).first()

    if db_hotel is None:
        raise HTTPException(status_code=404, detail = 'Not Found')
    return db_hotel

@hotel_router.put('/{hotel_id}', response_model=dict)
async def hotel_update(hotel : HotelCreateSchema,hotel_id: int,
                         db : Session = Depends(get_db)):
    db_hotel = db.query(Hotel).filter(Hotel.id == hotel_id).first()
    if not db_hotel:
        raise HTTPException(status_code=404, detail = 'Not Found')
    for hotel_key , hotel_value in hotel.dict().items():
        setattr(db_hotel , hotel_key,hotel_value)

        db.commit()
        db.refresh(db_hotel)

        return {'message':'Успешно!'}


@hotel_router.delete('/{hotel_id}/', response_model=dict)
async def hotel_delete(hotel_id: int, db: Session = Depends(get_db)):
    db_hotel = db.query(Hotel).filter(Hotel.id == hotel_id).first()
    if db_hotel is None:
        raise HTTPException(status_code=404, detail = 'Product Not Found')
    db.delete(db_hotel)
    db.commit()
    return {'message': 'Удалено!'}


