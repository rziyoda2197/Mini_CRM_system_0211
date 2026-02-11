from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas

router = APIRouter(prefix="/clients", tags=["Clients"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create(data: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db, data)


@router.get("/")
def list_clients(db: Session = Depends(get_db)):
    return crud.get_clients(db)


@router.delete("/{client_id}")
def delete(client_id: int, db: Session = Depends(get_db)):
    crud.delete_client(db, client_id)
    return {"deleted": True}
