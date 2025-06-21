from .views import *
from fastapi import FastAPI
from sqladmin import Admin
from booking_app.db.database import first

def setup_admin(store_app:FastAPI):
    admin = Admin(store_app, first)
    admin.add_view(UserProfileAdmin)
    admin.add_view(HotelAdmin)
    admin.add_view(RoomAdmin)
    admin.add_view(ReviewsAdmin)
    admin.add_view(CountryAdmin)
    admin.add_view(CityAdmin)