from pydantic import BaseModel , EmailStr
from typing import Optional
from .models import STATUS_CHOICES
from datetime import datetime

class UserProfileCreateSchema(BaseModel):
    last_name : str
    first_name : str
    username : str
    phone_number : Optional[str]
    age : Optional[int]
    email : EmailStr
    status : STATUS_CHOICES
    password : str

    class Config:
        from_attributes = True


class UserProfileLoginSchema(BaseModel):
    username : str
    password : str

    class Config:
        from_attributes = True


class UserProfileGetSchema(BaseModel):
    id: int
    last_name : str
    first_name : str
    username : str
    phone_number : Optional[str]
    age : Optional[int]
    email : EmailStr
    status : STATUS_CHOICES
    password : str
    created_date : datetime


    class Config:
        from_attributes = True


class CountrySchema(BaseModel):
    id: int
    country_name: str

    class Config:
        from_attributes = True

class CitySchema(BaseModel):
    id: int
    city_name : str
    country_id : int

    class Config:
        from_attributes = True

class CityCreateSchema(BaseModel):
    city_name : str
    country_id : int

    class Config:
        from_attributes = True

class HotelGetSchema(BaseModel):
    id : int
    hotel_name : str
    phone_number : str
    description : str
    hotel_stars: int
    city_id : int

    class Config:
        from_attributes = True

class HotelCreateSchema(BaseModel):
    hotel_name : str
    phone_number : str
    description : str
    hotel_stars: int
    city_id : int

    class Config:
        from_attributes = True

class RoomSchema(BaseModel):
    id: int
    room_number : int
    description : str
    price : int
    hotel_id : int
    city_id : int

    class Config:
        from_attributes = True


class RoomCreateSchema(BaseModel):
    room_number : int
    description : str
    price : int
    hotel_id : int
    city_id : int

    class Config:
        from_attributes = True


class ReviewSchema(BaseModel):
    id: int
    comment : str
    stars : int
    author_id : int
    hotel_id : int
    created_date : datetime

    class Config:
        from_attributes = True

class ReviewCreateSchema(BaseModel):
    comment : str
    stars : int
    author_id : int
    hotel_id : int

    class Config:
        from_attributes = True

class BookingSchema(BaseModel):
    id: int
    user_id : int
    hotel_id : int
    room_id : int
    check_in : datetime
    check_out : datetime
    created_date : datetime

    class Config:
        from_attributes = True

class BookingCreateSchema(BaseModel):
    user_id : int
    hotel_id : int
    room_id : int
    check_in : datetime
    check_out : datetime

    class Config:
        from_attributes = True

