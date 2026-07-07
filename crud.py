from sqlalchemy.orm import Session
from models import EmployeeDB
from schemas import EmployeeCreate


def get_employees(db: Session):
    return db.query(EmployeeDB).all()


def get_employee(db: Session, emp_id: int):
    return db.query(EmployeeDB).filter(EmployeeDB.id == emp_id).first()


def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = EmployeeDB(
        name=employee.name,
        age=employee.age,
        dep=employee.dep,
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(db: Session, emp_id: int, employee: EmployeeCreate):
    db_employee = db.query(EmployeeDB).filter(EmployeeDB.id == emp_id).first()
    if not db_employee:
        return None
    db_employee.name = employee.name
    db_employee.age = employee.age
    db_employee.dep = employee.dep
    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, emp_id: int):
    db_employee = db.query(EmployeeDB).filter(EmployeeDB.id == emp_id).first()
    if not db_employee:
        return None
    db.delete(db_employee)
    db.commit()
    return db_employee
