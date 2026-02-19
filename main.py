from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routes import employee, attendance

Base.metadata.create_all(bind=engine)

app = FastAPI(title="HRMS Lite API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174", "http://127.0.0.1:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee.router, prefix="/api/employees", tags=["Employees"])
app.include_router(attendance.router, prefix="/api/attendance", tags=["Attendance"])

@app.get("/")
def root():
    return {"status": "HRMS Lite API running"}

