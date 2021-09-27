#!/usr/bin/env python3

from app.db.session import get_db
from app.db.crud import create_user
from app.db.schemas import UserCreate
from app.db.session import SessionLocal

import requests

def init() -> None:
    db = SessionLocal()

    create_user(
        db,
        UserCreate(
            email="admin@pos.com",
            password="password",
            is_active=True,
            is_superuser=True,
        ),
    )
    r = requests.get('https://wichit2s.gitlab.io/python/_static/data/Thailand-Provinces.json').json()
    for x in r:
        print(x['PROVINCE'], x['COUNTY'])
        # create_province()



if __name__ == "__main__":
    print("Creating superuser admin@pos.com")
    init()
    print("Superuser created")
