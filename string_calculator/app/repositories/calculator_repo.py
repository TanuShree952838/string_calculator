from sqlalchemy.orm import Session

from string_calculator.app.models.calculation import Calculation

def save_calculation(db: Session, input_data: str, result: int):
    calc = Calculation(input_data=input_data, result=result)
    db.add(calc)
    db.commit()
    db.refresh(calc)
    return calc
