import anvil.secrets
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, Identity(start=42, cycle=True), primary_key=True) # we do this differently, this might be wrong
    email = Column(String, unique=True, nullable=False)
    name = Column(String)

    def __repr__(self):
        return f"<Employee(email='{self.email}', name='{self.name}', id='{self.id}')>"