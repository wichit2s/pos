from sqlalchemy import Boolean, Column, Integer, String, Float

from .session import Base


class User(Base):
    __tablename__ = "user"

    id              = Column(Integer, primary_key=True, index=True)
    email           = Column(String, unique=True, index=True, nullable=False)
    first_name      = Column(String)
    last_name       = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active       = Column(Boolean, default=True)
    is_superuser    = Column(Boolean, default=False)

class Province(Base):
    __tablename__ = "province"

    id              = Column(Integer, primary_key=True, index=True)
    province        = Column(String)
    county          = Column(String)
    image           = Column(String)
    lat             = Column(Float)
    lng             = Column(Float)
