from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from database import engine, get_db
from models import EmployeeDB
from schemas import EmployeeCreate, EmployeeResponse
import crud

# Create all tables on startup
from database import Base
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/employees", response_model=List[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


@app.get("/employees/{emp_id}", response_model=EmployeeResponse)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.post("/employees", response_model=EmployeeResponse)
def add_employee(new_emp: EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, new_emp)


@app.put("/update_employee/{emp_id}", response_model=EmployeeResponse)
def update_employee(emp_id: int, updated_emp: EmployeeCreate, db: Session = Depends(get_db)):
    employee = crud.update_employee(db, emp_id, updated_emp)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.delete("/delete_employee/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}
