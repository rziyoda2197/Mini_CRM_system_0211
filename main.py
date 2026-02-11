from fastapi import FastAPI
from database import Base, engine
from routers import clients

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini CRM")

app.include_router(clients.router)
