from fastapi import HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm.session import Session
from db.models import User, Club, Event

def count_users(db: Session):
    return db.query(func.count(User.USER_ID)).scalar()

def total_distance(db: Session):
    return db.query(func.sum(User.TOTAL_DISTANCE)).scalar()

def total_club(db: Session):
    return db.query(func.count(Club.CLUB_ID)).scalar()

def total_race(db: Session):
    return db.query(func.count(Event.EVENT_ID)).scalar()