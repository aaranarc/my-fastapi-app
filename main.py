from fastapi import FastAPI, HTTPException
from models import Employee
from typing import List

emp: List[Employee] =[]

app = FastAPI()
@app.get("/employees",response_model=List[Employee])
def get_employees():
    return emp

@app.get("/employees/{emp_id}",response_model=Employee)
def get_employee(emp_id:int):
    for index, e in enumerate(emp):
        if e.id == emp_id:
            return emp[index]
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/employees")
def add_employee(new_emp: Employee):
    for employee in emp:
        if employee.id == new_emp.id:
            raise HTTPException(status_code=400, detail="Employee with this ID already exists")
    emp.append(new_emp)
    return {"message": "Employee added successfully"}

@app.put("/update_employee/{emp_id}")
def update_employee(emp_id: int, updated_emp: Employee):
    for index, e in enumerate(emp):
        if e.id == emp_id:
            emp[index] = updated_emp
            return {"message": "Employee updated successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete("/delete_employee/{emp_id}")
def delete_employee(emp_id: int):
    for index, e in enumerate(emp):
        if e.id == emp_id:
            del emp[index]
            return {"message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")



