from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/support_cases/", response_model=schemas.SupportCase)
def create_support_case(case: schemas.SupportCaseCreate, db: Session = Depends(get_db)):
    return crud.create_support_case(db=db, case=case)

@router.get("/support_cases/{case_id}", response_model=schemas.SupportCase)
def read_support_case(case_id: int, db: Session = Depends(get_db)):
    db_case = crud.get_support_case(db, case_id=case_id)
    if db_case is None:
        raise HTTPException(status_code=404, detail="Support case not found")
    return db_case
