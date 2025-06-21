from fastapi import FastAPI
import uvicorn
from booking_app.admin.setup import setup_admin
from booking_app.api import country,city,auth, hotel, room , review , booking , social_account
from starlette.middleware.sessions import SessionMiddleware
from booking_app.config import SECRET_KEY


booking_app = FastAPI()
booking_app.include_router(country.country_router)
booking_app.include_router(city.city_router)
booking_app.include_router(auth.auth_router)
booking_app.include_router(hotel.hotel_router)
booking_app.include_router(room.room_router)
booking_app.include_router(review.reviews_router)
booking_app.include_router(booking.booking_router)
booking_app.include_router(social_account.social_router)
booking_app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
setup_admin(booking_app)



if __name__ == '__main__':
    uvicorn.run(booking_app ,host='127.0.0.1' , port=8000)