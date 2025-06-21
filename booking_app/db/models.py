from .database import Base
from sqlalchemy import ForeignKey,String,Integer ,DateTime,Enum , Text, Boolean, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column,relationship
from datetime import datetime
from typing import  Optional,List
from enum import Enum as PyEnum

class STATUS_CHOICES(str, PyEnum):
        client ='client',
        owner = 'owner'

class UserProfile(Base):
    __tablename__ = 'userprofile'

    id : Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    last_name: Mapped[str] = mapped_column(String(32))
    first_name : Mapped[str] = mapped_column(String(32))
    username : Mapped[str] = mapped_column(String(32),nullable=False)
    phone_number : Mapped[Optional[str]] = mapped_column(String, nullable=True)
    age : Mapped[Optional[int]] = mapped_column(Integer,nullable=True)
    email : Mapped[str] = mapped_column(String)
    status : Mapped[STATUS_CHOICES] = mapped_column(Enum(STATUS_CHOICES) , default=STATUS_CHOICES.client)
    password : Mapped[str] = mapped_column(String)
    create_date : Mapped[datetime] = mapped_column(DateTime,default=datetime.utcnow)
    reviews : Mapped[List['Review']] = relationship('Review' , back_populates='author',
                                                    cascade='all , delete-orphan')
    booking_user : Mapped[List['Booking']] = relationship('Booking', back_populates='user',
                                                          cascade='all , delete-orphan')

    user : Mapped[List['RefreshToken']] = relationship('RefreshToken', back_populates='user',
                                                          cascade='all , delete-orphan')

    def __str__(self):
        return f'{self.first_name} , {self.last_name}'


class RefreshToken(Base):
    __tablename__= 'refresh_token'

    id : Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey('userprofile.id'))
    user : Mapped[UserProfile] = relationship(UserProfile , back_populates='user')
    token : Mapped[str] = mapped_column(String , nullable=False)
    create_date : Mapped[datetime] = mapped_column(DateTime,default=datetime.utcnow)



class Country(Base):
    __tablename__ = 'country'

    id : Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    country_name : Mapped[str] = mapped_column(String)
    city_country : Mapped[List['City']] = relationship('City' , back_populates='country',
                                                             cascade='all , delete-orphan')

    def __repr__(self):
        return f'{self.country_name}'

class City(Base):
    __tablename__ = 'city'

    id : Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    city_name : Mapped[str] = mapped_column(String)
    country_id : Mapped[int] = mapped_column(ForeignKey('country.id'))
    country : Mapped[Country] = relationship(Country, back_populates='city_country')
    city_hotel : Mapped[List['Hotel']] = relationship('Hotel' , back_populates='city',
                                                      cascade='all , delete-orphan')
    city_room : Mapped[List['Room']] = relationship('Room' , back_populates='city',
                                                    cascade='all , delete-orphan')

    def __repr__(self):
        return f'{self.city_name}'

class Hotel(Base):
    __tablename__ = 'hotel'

    id : Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    hotel_name : Mapped[str] = mapped_column(String)
    phone_number : Mapped[str] = mapped_column(String)
    description : Mapped[str] = mapped_column(Text)
    hotel_stars : Mapped[int] = mapped_column(Integer)
    city_id : Mapped[int] = mapped_column(ForeignKey('city.id'))
    city : Mapped[City] = relationship(City, back_populates='city_hotel')
    room_hotel : Mapped[List['Room']] = relationship('Room' , back_populates='hotel',
                                                     cascade='all , delete-orphan')
    reviews_hotel : Mapped[List['Review']] = relationship('Review' , back_populates='hotel',
                                                          cascade='all , delete-orphan')
    booking_hotel :  Mapped[List['Booking']] = relationship('Booking' , back_populates='hotel',
                                                          cascade='all , delete-orphan')

    def __repr__(self):
        return f'{self.hotel_name}'

class Room(Base):
    __tablename__ = 'room'

    id : Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    room_number : Mapped[int] = mapped_column(Integer)
    description : Mapped[str] = mapped_column(Text)
    price : Mapped[int] = mapped_column(Integer)
    hotel_id : Mapped[int] = mapped_column(ForeignKey('hotel.id'))
    hotel : Mapped[Hotel] = relationship(Hotel, back_populates= 'room_hotel')
    city_id : Mapped[int] = mapped_column(ForeignKey('city.id'))
    city : Mapped[City] = relationship(City, back_populates='city_room')
    booking_room : Mapped[List['Booking']] = relationship('Booking', back_populates='room',
                                                          cascade='all , delete-orphan')


class Review(Base):
    __tablename__ = 'review'

    id : Mapped[int] = mapped_column(Integer, autoincrement=True , primary_key=True)
    comment : Mapped[str | None] = mapped_column(Text, nullable=True)
    stars : Mapped[int | None] = mapped_column(Integer, nullable=True)
    author_id : Mapped[int] = mapped_column(ForeignKey('userprofile.id'))
    author : Mapped[UserProfile] = relationship(UserProfile , back_populates='reviews')
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotel.id'))
    hotel : Mapped[Hotel] = relationship(Hotel , back_populates='reviews_hotel')
    created_date : Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Booking(Base):
    __tablename__ = 'booking'

    id : Mapped[int] = mapped_column(Integer, autoincrement=True , primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey('userprofile.id'))
    user : Mapped[UserProfile] = relationship(UserProfile , back_populates='booking_user')
    hotel_id : Mapped[int] = mapped_column(ForeignKey('hotel.id'))
    hotel: Mapped[Hotel] = relationship(Hotel , back_populates='booking_hotel')
    room_id : Mapped[int] = mapped_column(ForeignKey('room.id'))
    room : Mapped[Room] = relationship(Room, back_populates='booking_room')
    check_in : Mapped[datetime] = mapped_column(DateTime)
    check_out : Mapped[datetime] = mapped_column(DateTime)
    created_date : Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
