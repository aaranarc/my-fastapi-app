# 🚀 My FastAPI App

A simple Employee Management REST API built with **FastAPI** and **Pydantic**.

## 📁 Project Structure

```
my-fastapi-app/
├── main.py              # Employee CRUD API
├── models.py            # Pydantic Employee model
├── pydantic_demo.py     # Pydantic demo with a User endpoint
├── .gitignore
└── README.md
```

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — Modern, high-performance Python web framework
- [Pydantic](https://docs.pydantic.dev/) — Data validation using Python type hints
- [Uvicorn](https://www.uvicorn.org/) — ASGI server to run the app

## 📦 Setup

```bash
# Clone the repo
git clone https://github.com/aaranarc/my-fastapi-app.git
cd my-fastapi-app

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn pydantic
```

## ▶️ Run the App

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

Interactive docs at `http://127.0.0.1:8000/docs`

## 📡 API Endpoints

### Employee API (`main.py`)

| Method   | Endpoint                      | Description              |
|----------|-------------------------------|--------------------------|
| `GET`    | `/employees`                  | Get all employees        |
| `GET`    | `/employees/{emp_id}`         | Get employee by ID       |
| `POST`   | `/employees`                  | Add a new employee       |
| `PUT`    | `/update_employee/{emp_id}`   | Update an employee       |
| `DELETE` | `/delete_employee/{emp_id}`   | Delete an employee       |

### Employee Model

```json
{
  "id": 1,
  "name": "Aarana",
  "age": 25,
  "dep": "Engineering"
}
```

### Pydantic Demo (`pydantic_demo.py`)

| Method | Endpoint | Description          |
|--------|----------|----------------------|
| `GET`  | `/user`  | Returns a sample user |

## 📝 License

Feel free to use this project for learning and experimentation.
