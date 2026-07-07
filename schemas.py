from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    name: str
    age: int
    dep: str


class EmployeeResponse(BaseModel):
    id: int
    name: str
    age: int
    dep: str

    class Config:
        from_attributes = True
