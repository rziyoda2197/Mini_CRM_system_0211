from models import Client

def create_client(db, data):
    client = Client(**data.dict())
    db.add(client)
    db.commit()
    db.refresh(client)
    return client


def get_clients(db):
    return db.query(Client).all()


def delete_client(db, client_id):
    client = db.query(Client).get(client_id)
    if client:
        db.delete(client)
        db.commit()
