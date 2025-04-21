from sqlalchemy import Column, Integer, String

from string_calculator.app.database.connection import Base

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    input_data = Column(String, nullable=False)
    result = Column(Integer, nullable=False)
