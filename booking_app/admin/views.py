from pydantic_core.core_schema import model_field

from booking_app.db.models import UserProfile,Hotel,Room,Review,Country,City,Booking

from sqladmin import ModelView

class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [UserProfile.first_name, UserProfile.last_name]

class HotelAdmin(ModelView, model=Hotel):
    column_list = [Hotel.id , Hotel.hotel_name]

class RoomAdmin(ModelView , model= Room):
    column_list = [Room.room_number, Room.id]

class ReviewsAdmin(ModelView , model = Review):
    column_list = [Review.author ]

class CountryAdmin(ModelView, model = Country):
    column_list = [Country.id , Country.country_name]

class CityAdmin(ModelView, model = City):
    column_list = [City.id, City.city_name]