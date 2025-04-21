from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

from string_calculator.app.database.connection import get_db
from string_calculator.app.repositories.calculator_repo import save_calculation
from string_calculator.app.services.calculator_service import add_numbers

router = APIRouter()

@router.post("/add")
def calculate_sum(data: str, db: Session = Depends(get_db)):
    try:
        result, negatives = add_numbers(data.numbers)
        if negatives:
            raise HTTPException(status_code=400, detail=f"Negative numbers not allowed: {', '.join(map(str, negatives))}")
        save_calculation(db, data.numbers, result)
        return {"sum": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
