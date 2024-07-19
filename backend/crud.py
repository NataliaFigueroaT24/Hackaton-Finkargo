from sqlalchemy.orm import Session
from . import models, schemas

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_support_case(db: Session, case_id: int):
    return db.query(models.SupportCase).filter(models.SupportCase.id == case_id).first()

def create_support_case(db: Session, case: schemas.SupportCaseCreate):
    db_case = models.SupportCase(title=case.title, description=case.description)
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case


