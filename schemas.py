from pydantic import BaseModel

class ClientCreate(BaseModel):
    name: str
    phone: str
    note: str


class ClientOut(BaseModel):
    id: int
    name: str
    phone: str
    note: str

    class Config:
        from_attributes = True
